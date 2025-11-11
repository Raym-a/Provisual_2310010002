from PySide6.QtWidgets import (
    QApplication, QWidget, QHeaderView, QMessageBox,
    QFileDialog, QTableWidgetItem
)
from PySide6.QtCore import QFile, Qt, QDate
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets, QtCore

# Import file CRUD
from crud_Pemesanan import crudPemesanan
from crud_Konsumen import crudKonsumen  # agar loadKonsumenKeCombo() bisa ambil daftar konsumen


class pemesanan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('ui_Pemesanan.ui')
        filenya.open(QFile.ReadOnly)

        muatFile = QUiLoader()
        self.ui_Pemesanan = muatFile.load(filenya, self)

        # Coding Untuk Rumus Button/CRUD Terhubung
        self.aksiCrud = crudPemesanan()

        # Coding untuk ambil data konsumen Karena ada Relasi ComboBox
        self.aksiKonsumen = crudKonsumen()

        # Untuk Memanggil Data ketika pertama kali dibuka
        self.loadDataPemesanan()
        self.loadKonsumenKeCombo()

        # Untuk Memanggil Otomatis table Input ketika klik Data di Widget
        self.ui_Pemesanan.TabelPemesanan.cellClicked.connect(self.tampilDataKeForm)

        # Digunakan untuk Judul Kolom Otomatis ditengah lebar Kolom
        self.ui_Pemesanan.TabelPemesanan.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # Coding Untuk Penghubung Button Pemesanan
        self.ui_Pemesanan.btnTambahPemesanan.clicked.connect(self.aksiSimpanPemesanan)
        self.ui_Pemesanan.btnEditPemesanan.clicked.connect(self.aksiEditPemesanan)
        self.ui_Pemesanan.btnHapusPemesanan.clicked.connect(self.aksiHapusPemesanan)

        self.ui_Pemesanan.editCari.textChanged.connect(self.aksiCariPemesanan)


    ## Coding Untuk Rumus / Cara Button Bekerja

    # ============ SIMPAN ============
    def aksiSimpanPemesanan(self):
        if not self.ui_Pemesanan.txtIdPemesanan.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Pemesanan tidak boleh kosong!")
            return
        elif self.ui_Pemesanan.cbKonsumen.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Konsumen harus dipilih!")
            return
        elif not self.ui_Pemesanan.txtProdukDipesan.text().strip():
            QMessageBox.warning(self, "Peringatan", "Produk Dipesan tidak boleh kosong!")
            return
        elif not self.ui_Pemesanan.txtTotalHarga.text().strip():
            QMessageBox.warning(self, "Peringatan", "Total Harga tidak boleh kosong!")
            return
        elif self.ui_Pemesanan.cbStatusPemesanan.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Status harus dipilih!")
            return
        else:
            idpem = self.ui_Pemesanan.txtIdPemesanan.text()
            idkon = self.ui_Pemesanan.cbKonsumen.currentData()
            produk = self.ui_Pemesanan.txtProdukDipesan.text()
            tgl = self.ui_Pemesanan.datePemesanan.date().toString("yyyy-MM-dd")
            talhar = self.ui_Pemesanan.txtTotalHarga.text()
            sts = self.ui_Pemesanan.cbStatusPemesanan.currentText()

            # Simpan ke database
            self.aksiCrud.simpanPemesanan(idpem, idkon, produk, tgl, talhar, sts)

            # Refresh tabel
            self.loadDataPemesanan()

            # Kosongkan form
            self.resetFormPemesanan()

            QMessageBox.information(self, "Berhasil", "Data pemesanan berhasil disimpan.")

    # ============ EDIT ============
    def aksiEditPemesanan(self):
        if not self.ui_Pemesanan.txtIdPemesanan.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Pemesanan tidak boleh kosong!")
            return
        elif self.ui_Pemesanan.cbKonsumen.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Konsumen harus dipilih!")
            return
        elif not self.ui_Pemesanan.txtProdukDipesan.text().strip():
            QMessageBox.warning(self, "Peringatan", "Produk Dipesan tidak boleh kosong!")
            return
        elif not self.ui_Pemesanan.txtTotalHarga.text().strip():
            QMessageBox.warning(self, "Peringatan", "Total Harga tidak boleh kosong!")
            return
        elif self.ui_Pemesanan.cbStatusPemesanan.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Status harus dipilih!")
            return
        else:
            idpem = self.ui_Pemesanan.txtIdPemesanan.text()
            idkon = self.ui_Pemesanan.cbKonsumen.currentData()
            produk = self.ui_Pemesanan.txtProdukDipesan.text()
            tgl = self.ui_Pemesanan.datePemesanan.date().toString("yyyy-MM-dd")
            talhar = self.ui_Pemesanan.txtTotalHarga.text()
            sts = self.ui_Pemesanan.cbStatusPemesanan.currentText()

            # Simpan Ke Database
            self.aksiCrud.editPemesanan(idpem, idkon, produk, tgl, talhar, sts)

            # Refresh tabel
            self.loadDataPemesanan()

            # Kosongkan form
            self.resetFormPemesanan()

            QMessageBox.information(self, "Berhasil", f"Data pemesanan '{idpem}' berhasil diperbarui.")

    # ============ HAPUS ============
    def aksiHapusPemesanan(self):
        idpem = self.ui_Pemesanan.txtIdPemesanan.text().strip()
        if idpem == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus terlebih dahulu!")
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus data pemesanan dengan ID '{idpem}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            # Hapus Data dari Database
            self.aksiCrud.hapusPemesanan(idpem)

            # Refresh Tabel
            self.loadDataPemesanan()

            # Mengosongkan Form Input
            self.resetFormPemesanan()

            QMessageBox.information(self, "Berhasil", f"Data pemesanan '{idpem}' berhasil dihapus.")

    # ============ LOAD DATA ============
    def loadDataPemesanan(self, data=None):
        if data is None:
            data = self.aksiCrud.tampilPemesanan()

        tabel = self.ui_Pemesanan.TabelPemesanan
        tabel.setRowCount(0)

        # Mapping ID Konsumen → Nama Konsumen
        konsumen_dict = {row[0]: row[1] for row in self.aksiKonsumen.tampilKonsumen()}

        # Set kolom
        tabel.setColumnCount(6)
        tabel.setHorizontalHeaderLabels([
            "ID Pemesanan", "Nama Konsumen", "Produk Dipesan",
            "Tanggal Pemesanan", "Total Harga", "Status"
        ])

        # Isi data ke tabel
        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)
            for column_number, cell_data in enumerate(row_data):
                if column_number == 1:  # Ganti ID konsumen jadi nama
                    cell_data = konsumen_dict.get(cell_data, cell_data)
                tabel.setItem(
                    row_number,
                    column_number,
                    QtWidgets.QTableWidgetItem(str(cell_data))
                )

        # Pengaturan header agar tidak terpotong
        header = tabel.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignCenter)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        tabel.resizeRowsToContents()

    # ============ TAMPILKAN DATA KE FORM ============
    def tampilDataKeForm(self, row, column):
        tabel = self.ui_Pemesanan.TabelPemesanan

        id_pemesanan = tabel.item(row, 0).text()
        nama_konsumen = tabel.item(row, 1).text()
        produk_dipesan = tabel.item(row, 2).text()
        tanggal_pemesanan = tabel.item(row, 3).text()
        total_harga = tabel.item(row, 4).text()
        status = tabel.item(row, 5).text()

        # Masukkan data ke form input
        self.ui_Pemesanan.txtIdPemesanan.setText(id_pemesanan)
        self.ui_Pemesanan.txtProdukDipesan.setText(produk_dipesan)
        self.ui_Pemesanan.txtTotalHarga.setText(total_harga)

        # ==== Atur tanggal ke QDateEdit ====
        try:
            qdate = QDate.fromString(tanggal_pemesanan, "yyyy-MM-dd")
            if qdate.isValid():
                self.ui_Pemesanan.datePemesanan.setDate(qdate)
        except Exception:
            pass

        # ==== Atur ComboBox Konsumen ====
        for i in range(self.ui_Pemesanan.cbKonsumen.count()):
            teks_combo = self.ui_Pemesanan.cbKonsumen.itemText(i)
            if teks_combo.startswith(nama_konsumen):
                self.ui_Pemesanan.cbKonsumen.setCurrentIndex(i)
                break

        # ==== Atur ComboBox Status ====
        index_status = self.ui_Pemesanan.cbStatusPemesanan.findText(status, Qt.MatchFixedString)
        if index_status >= 0:
            self.ui_Pemesanan.cbStatusPemesanan.setCurrentIndex(index_status)

    # ============ LOAD KONSUMEN ============
    def loadKonsumenKeCombo(self):
        data = self.aksiKonsumen.tampilKonsumen()
        self.ui_Pemesanan.cbKonsumen.clear()

        # Coding baris ini untuk menambahkan teks
        self.ui_Pemesanan.cbKonsumen.addItem("Pilih Konsumen", None)

        # Rumus untuk Menampilkan isi Database dari Tabel Konsumen
        for row in data:
            id_konsumen = row[0]
            nama_perusahaan = row[1]
            tampil_combo = f"{nama_perusahaan} - {id_konsumen}"
            self.ui_Pemesanan.cbKonsumen.addItem(tampil_combo, id_konsumen)

        # Coding untuk awal dibuka  di posisi "Pilih Konsumen"
        self.ui_Pemesanan.cbKonsumen.setCurrentIndex(0)


    def aksiCariPemesanan(self):
        nama = self.ui_Pemesanan.editCari.text().strip()

        if nama == "":
            # Jika kolom cari kosong, tampilkan semua data
            data = self.aksiCrud.tampilPemesanan()
        else:
            # Jika ada teks, filter berdasarkan nama konsumen
            data = self.aksiCrud.filterKonsumen(nama)

        # Update tabel dengan data yang difilter
        self.loadDataPemesanan(data)


    # ============ RESET FORM ============
    def resetFormPemesanan(self):
        self.ui_Pemesanan.txtIdPemesanan.clear()
        self.ui_Pemesanan.txtProdukDipesan.clear()
        self.ui_Pemesanan.txtTotalHarga.clear()
        self.ui_Pemesanan.datePemesanan.setDate(QtCore.QDate.currentDate())
        self.ui_Pemesanan.cbKonsumen.setCurrentIndex(0)
        self.ui_Pemesanan.cbStatusPemesanan.setCurrentIndex(0)
