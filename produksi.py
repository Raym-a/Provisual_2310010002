from PySide6.QtWidgets import (
    QApplication, QWidget, QHeaderView, QMessageBox,
    QFileDialog, QTableWidgetItem
)
from PySide6.QtCore import QFile, Qt, QDate
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets, QtCore

# Import File CRUD
from crud_Produksi import crudProduksi
from crud_Konsumen import crudKonsumen
from crud_Pemesanan import crudPemesanan



class produksi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('ui_Produksi.ui')
        filenya.open(QFile.ReadOnly)

        muatFile = QUiLoader()
        self.ui_Produksi = muatFile.load(filenya, self)

        # Coding Untuk Rumus Button/CRUD Terhubung
        self.aksiProduksi = crudProduksi()

        # Coding untuk ambil data konsumen Karena ada Relasi ComboBox
        self.aksiKonsumen = crudKonsumen()

        # Coding untuk ambil data pemesanan Karena ada relasi dengan Produksi
        self.aksiPemesanan = crudPemesanan()

        # Untuk memanggil data combobox Pemesanan saat pertama dibuka
        self.loadPemesananKeCombo()

        # Untuk Memanggil Data ketika pertama kali dibuka
        self.loadDataProduksi()


        # Untuk Memanggil Otomatis table Input ketika klik Data di Widget
        self.ui_Produksi.TabelProduksi.cellClicked.connect(self.tampilDataKeFormProduksi)

        # Digunakan untuk Judul Kolom Otomatis ditengah lebar Kolom
        self.ui_Produksi.TabelProduksi.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # Coding Untuk Penghubung Button Produksi
        self.ui_Produksi.btnTambahProduksi.clicked.connect(self.aksiSimpanProduksi)
        self.ui_Produksi.btnEditProduksi.clicked.connect(self.aksiEditProduksi)
        self.ui_Produksi.btnHapusProduksi.clicked.connect(self.aksiHapusProduksi)

        self.ui_Produksi.editCari.textChanged.connect(self.aksiCariProduksi)

    ## Coding Untuk Rumus / Cara Button Bekerja


    # ============ SIMPAN ============
    def aksiSimpanProduksi(self):
        if not self.ui_Produksi.txtIdProduksi.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Produksi tidak boleh kosong!")
            return
        elif self.ui_Produksi.cbPemesanan.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Pemesanan harus dipilih!")
            return
        elif not self.ui_Produksi.dateProduksi.date().toString("yyyy-MM-dd"):
            QMessageBox.warning(self, "Peringatan", "Tanggal Produksi harus dipilih!")
            return
        elif not self.ui_Produksi.txtJumlahProduksi.text().strip():
            QMessageBox.warning(self, "Peringatan", "Jumlah Produksi tidak boleh kosong!")
            return
        elif not self.ui_Produksi.txtKeterangan.toPlainText().strip():
            QMessageBox.warning(self, "Peringatan", "Keterangan tidak boleh kosong!")
            return
        else:
            idpro = self.ui_Produksi.txtIdProduksi.text()
            idpem = self.ui_Produksi.cbPemesanan.currentData()
            tgpro = self.ui_Produksi.dateProduksi.date().toString("yyyy-MM-dd")
            jumsi = self.ui_Produksi.txtJumlahProduksi.text()
            ket = self.ui_Produksi.txtKeterangan.toPlainText()

            # Simpan ke database
            self.aksiProduksi.simpanProduksi(idpro, idpem, tgpro, jumsi, ket)

            # Refresh tabel
            self.loadDataProduksi()

            # Kosongkan form
            self.resetFormProduksi()

            QMessageBox.information(self, "Berhasil", "Data produksi berhasil disimpan.")


    # ============ EDIT ============
    def aksiEditProduksi(self):
        if not self.ui_Produksi.txtIdProduksi.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Produksi tidak boleh kosong!")
            return
        elif self.ui_Produksi.cbPemesanan.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Pemesanan harus dipilih!")
            return
        elif not self.ui_Produksi.dateProduksi.date().toString("yyyy-MM-dd"):
            QMessageBox.warning(self, "Peringatan", "Tanggal Produksi harus dipilih!")
            return
        elif not self.ui_Produksi.txtJumlahProduksi.text().strip():
            QMessageBox.warning(self, "Peringatan", "Jumlah Produksi tidak boleh kosong!")
            return
        elif not self.ui_Produksi.txtKeterangan.toPlainText().strip():
            QMessageBox.warning(self, "Peringatan", "Keterangan tidak boleh kosong!")
            return
        else:
            idpro = self.ui_Produksi.txtIdProduksi.text()
            idpem = self.ui_Produksi.cbPemesanan.currentData()
            tgpro = self.ui_Produksi.dateProduksi.date().toString("yyyy-MM-dd")
            jumsi = self.ui_Produksi.txtJumlahProduksi.text()
            ket = self.ui_Produksi.txtKeterangan.toPlainText()

            # Simpan ke database
            self.aksiProduksi.editProduksi(idpro, idpem, tgpro, jumsi, ket)

            # Refresh tabel
            self.loadDataProduksi()

            # Kosongkan form
            self.resetFormProduksi()

            QMessageBox.information(self, "Berhasil", "Data produksi berhasil dirubah.")


    # ============ HAPUS ============
    def aksiHapusProduksi(self):
        idpro = self.ui_Produksi.txtIdProduksi.text().strip()
        if idpro == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus terlebih dahulu!")
            return

        # Konfirmasi penghapusan
        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus data produksi dengan ID '{idpro}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            # Hapus data dari database
            self.aksiProduksi.hapusProduksi(idpro)

            # Refresh tabel
            self.loadDataProduksi()

            # Mengosongkan Form Input
            self.resetFormProduksi()

            QMessageBox.information(self, "Berhasil", f"Data produksi dengan ID '{idpro}' berhasil dihapus.")


    def loadDataProduksi(self, data=None):
        try:
            # Jika tidak ada data dikirim, ambil semua data dari database
            if data is None:
                data = self.aksiProduksi.tampilProduksi()

            tabel = self.ui_Produksi.TabelProduksi
            tabel.setRowCount(0)

            # Mapping ID Konsumen → Nama Konsumen
            konsumen_dict = {row[0]: row[1] for row in self.aksiKonsumen.tampilKonsumen()}

            # Mapping ID Pemesanan → ID Konsumen
            pemesanan_dict = {row[0]: row[1] for row in self.aksiPemesanan.tampilPemesanan()}

            # Set kolom tabel
            tabel.setColumnCount(5)
            tabel.setHorizontalHeaderLabels([
                "ID Produksi", "Nama Konsumen", "Tanggal Produksi",
                "Jumlah Produksi", "Keterangan"
            ])

            # Isi data ke tabel
            for row_number, row_data in enumerate(data):
                tabel.insertRow(row_number)

                id_produksi = row_data[0]
                id_pemesanan = row_data[1]
                tanggal_produksi = row_data[2]
                jumlah_produksi = row_data[3]
                keterangan = row_data[4]

                # Ambil ID konsumen dari id_pemesanan
                id_konsumen = pemesanan_dict.get(id_pemesanan)
                nama_konsumen = konsumen_dict.get(id_konsumen, "Tidak Diketahui")

                # Susun isi tabel
                row_items = [
                    id_produksi,
                    nama_konsumen,
                    tanggal_produksi,
                    jumlah_produksi,
                    keterangan
                ]

                for column_number, cell_data in enumerate(row_items):
                    tabel.setItem(
                        row_number,
                        column_number,
                        QtWidgets.QTableWidgetItem(str(cell_data))
                    )

            # Pengaturan tampilan tabel
            header = tabel.horizontalHeader()
            header.setDefaultAlignment(Qt.AlignCenter)
            header.setSectionResizeMode(QHeaderView.ResizeToContents)
            header.setStretchLastSection(True)
            tabel.resizeRowsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Kesalahan", f"Gagal memuat data produksi!\n\n{str(e)}")



    # ============ TAMPILKAN DATA KE FORM PRODUKSI ============
    def tampilDataKeFormProduksi(self, row, column):
        tabel = self.ui_Produksi.TabelProduksi

        # Ambil data dari tabel tampilan
        id_produksi = tabel.item(row, 0).text()
        tanggal_produksi = tabel.item(row, 2).text()
        jumlah_produksi = tabel.item(row, 3).text()
        keterangan = tabel.item(row, 4).text()

        # --- Ambil id_pemesanan dari database berdasarkan id_produksi ---
        try:
            cur = self.aksiProduksi.koneksi.cursor()
            cur.execute("SELECT id_pemesanan FROM produksi WHERE id_produksi=%s", (id_produksi,))
            hasil = cur.fetchone()
            cur.close()

            id_pemesanan = hasil[0] if hasil else None
        except Exception:
            id_pemesanan = None

        # --- Set nilai ke form input ---
        self.ui_Produksi.txtIdProduksi.setText(id_produksi)
        self.ui_Produksi.txtJumlahProduksi.setText(jumlah_produksi)
        self.ui_Produksi.txtKeterangan.setPlainText(keterangan)

        # === Atur tanggal ke QDateEdit ===
        try:
            qdate = QtCore.QDate.fromString(tanggal_produksi, "yyyy-MM-dd")
            if qdate.isValid():
                self.ui_Produksi.dateProduksi.setDate(qdate)
        except Exception:
            self.ui_Produksi.dateProduksi.setDate(QtCore.QDate.currentDate())

        # === Pilih item di ComboBox berdasarkan id_pemesanan ===
        combo = self.ui_Produksi.cbPemesanan
        index = combo.findData(id_pemesanan)  # cocokkan berdasarkan data (id)
        if index != -1:
            combo.setCurrentIndex(index)
        else:
            combo.setCurrentIndex(0)  # fallback ke "Pilih Pemesanan"


    # ============ LOAD PEMESANAN ============
    def loadPemesananKeCombo(self):
        try:
            data_pemesanan = self.aksiPemesanan.tampilPemesanan()
            data_konsumen = {row[0]: row[1] for row in self.aksiKonsumen.tampilKonsumen()}

            self.ui_Produksi.cbPemesanan.clear()

            # Tambahkan teks awal di ComboBox
            self.ui_Produksi.cbPemesanan.addItem("Pilih Pemesanan", None)

            # Tampilkan daftar Pemesanan + Nama Konsumen
            for row in data_pemesanan:
                id_pemesanan = row[0]
                id_konsumen = row[1]
                nama_konsumen = data_konsumen.get(id_konsumen, "Tidak Diketahui")

                tampil_combo = f"{id_pemesanan} - {nama_konsumen}"
                self.ui_Produksi.cbPemesanan.addItem(tampil_combo, id_pemesanan)

            # Atur posisi awal
            self.ui_Produksi.cbPemesanan.setCurrentIndex(0)

        except Exception as e:
            QMessageBox.critical(self, "Kesalahan", f"Gagal memuat data pemesanan!\n\n{str(e)}")

    def aksiCariProduksi(self):
        nama = self.ui_Produksi.editCari.text().strip()
        if nama == "":
            # Jika kolom cari kosong, tampilkan semua data
            data = self.aksiProduksi.tampilProduksi()
        else:
            # Jika ada teks, filter berdasarkan nama konsumen
            data = self.aksiProduksi.filterProduksi(nama)
            # Update tabel dengan data yang difilter
        self.loadDataProduksi(data)

    # ============ RESET FORM ============
    def resetFormProduksi(self):
        self.ui_Produksi.txtIdProduksi.clear()
        self.ui_Produksi.txtJumlahProduksi.clear()
        self.ui_Produksi.txtKeterangan.clear()
        self.ui_Produksi.dateProduksi.setDate(QtCore.QDate.currentDate())
        self.ui_Produksi.cbPemesanan.setCurrentIndex(0)


