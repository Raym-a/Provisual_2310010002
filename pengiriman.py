from PySide6.QtWidgets import (
    QApplication, QWidget, QHeaderView, QMessageBox,
    QFileDialog, QTableWidgetItem
)
from PySide6.QtCore import QFile, Qt, QDate
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets, QtCore

# Import File CRUD
from crud_Pengiriman import crudPengiriman
from crud_Konsumen import crudKonsumen
from crud_Pemesanan import crudPemesanan

class pengiriman(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('ui_Pengiriman.ui')
        filenya.open(QFile.ReadOnly)

        muatFile = QUiLoader()
        self.ui_Pengiriman = muatFile.load(filenya, self)

        # Coding Untuk Rumus Button/CRUD Terhubung
        self.aksiPengiriman = crudPengiriman()

        # Coding untuk ambil data konsumen Karena ada Relasi ComboBox
        self.aksiKonsumen = crudKonsumen()

        # Coding untuk ambil data pemesanan Karena ada relasi dengan Pengiriman
        self.aksiPemesanan = crudPemesanan()

        # Untuk memanggil data combobox Pemesanan saat pertama dibuka
        self.loadPemesananKeCombo()

        # Untuk Memanggil Data ketika pertama kali dibuka
        self.loadDataPengiriman()

        # Untuk Memanggil Otomatis table Input ketika klik Data di Widget
        self.ui_Pengiriman.TabelPengiriman.cellClicked.connect(self.tampilDataKeFormPengiriman)

        # Digunakan untuk Judul Kolom Otomatis ditengah lebar Kolom
        self.ui_Pengiriman.TabelPengiriman.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # Coding Untuk Penghubung Button Pengiriman
        self.ui_Pengiriman.btnTambahPengiriman.clicked.connect(self.aksiSimpanPengiriman)
        self.ui_Pengiriman.btnEditPengiriman.clicked.connect(self.aksiEditPengiriman)
        self.ui_Pengiriman.btnHapusPengiriman.clicked.connect(self.aksiHapusPengiriman)

        self.ui_Pengiriman.editCari.textChanged.connect(self.aksiCariPengiriman)

    ## Coding Untuk Rumus / Cara Button Bekerja

    # ============ SIMPAN ============
    def aksiSimpanPengiriman(self):
        if not self.ui_Pengiriman.txtIdPengiriman.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Pengiriman tidak boleh kosong!")
            return
        elif self.ui_Pengiriman.cbPemesanan.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Pemesanan harus dipilih!")
            return
        elif not self.ui_Pengiriman.datePengiriman.date().toString("yyyy-MM-dd"):
            QMessageBox.warning(self, "Peringatan", "Tanggal Pengiriman harus dipilih!")
            return
        elif not self.ui_Pengiriman.txtJumlahKirim.text().strip():
            QMessageBox.warning(self, "Peringatan", "Jumlah Kirim tidak boleh kosong!")
            return
        elif not self.ui_Pengiriman.txtKendaraan.text().strip():
            QMessageBox.warning(self, "Peringatan", "Kendaraan tidak boleh kosong!")
            return
        elif not self.ui_Pengiriman.txtSopir.text().strip():
            QMessageBox.warning(self, "Peringatan", "Sopir tidak boleh kosong!")
            return
        elif self.ui_Pengiriman.cbStatusPengiriman.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Status harus dipilih!")
            return
        else:
            idpeng = self.ui_Pengiriman.txtIdPengiriman.text()
            idpem = self.ui_Pengiriman.cbPemesanan.currentData()
            tgkirim = self.ui_Pengiriman.datePengiriman.date().toString("yyyy-MM-dd")
            jumkir = self.ui_Pengiriman.txtJumlahKirim.text()
            kendaraan = self.ui_Pengiriman.txtKendaraan.text()
            sopir = self.ui_Pengiriman.txtSopir.text()
            status = self.ui_Pengiriman.cbStatusPengiriman.currentText()

            # Simpan ke database
            self.aksiPengiriman.simpanPengiriman(idpeng, idpem, tgkirim, jumkir, kendaraan, sopir, status)

            # Refresh tabel
            self.loadDataPengiriman()

            # Kosongkan form
            self.resetFormPengiriman()

            QMessageBox.information(self, "Berhasil", "Data pengiriman berhasil disimpan.")

    # ============ EDIT ============
    def aksiEditPengiriman(self):
        if not self.ui_Pengiriman.txtIdPengiriman.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Pengiriman tidak boleh kosong!")
            return
        elif self.ui_Pengiriman.cbPemesanan.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Pemesanan harus dipilih!")
            return
        elif not self.ui_Pengiriman.datePengiriman.date().toString("yyyy-MM-dd"):
            QMessageBox.warning(self, "Peringatan", "Tanggal Pengiriman harus dipilih!")
            return
        elif not self.ui_Pengiriman.txtJumlahKirim.text().strip():
            QMessageBox.warning(self, "Peringatan", "Jumlah Kirim tidak boleh kosong!")
            return
        elif not self.ui_Pengiriman.txtKendaraan.text().strip():
            QMessageBox.warning(self, "Peringatan", "Kendaraan tidak boleh kosong!")
            return
        elif not self.ui_Pengiriman.txtSopir.text().strip():
            QMessageBox.warning(self, "Peringatan", "Sopir tidak boleh kosong!")
            return
        elif self.ui_Pengiriman.cbStatusPengiriman.currentIndex() == -1:
            QMessageBox.warning(self, "Peringatan", "Status harus dipilih!")
            return
        else:
            idpeng = self.ui_Pengiriman.txtIdPengiriman.text()
            idpem = self.ui_Pengiriman.cbPemesanan.currentData()
            tgkirim = self.ui_Pengiriman.datePengiriman.date().toString("yyyy-MM-dd")
            jumkir = self.ui_Pengiriman.txtJumlahKirim.text()
            kendaraan = self.ui_Pengiriman.txtKendaraan.text()
            sopir = self.ui_Pengiriman.txtSopir.text()
            status = self.ui_Pengiriman.cbStatusPengiriman.currentText()

            # Simpan ke database
            self.aksiPengiriman.editPengiriman(idpeng, idpem, tgkirim, jumkir, kendaraan, sopir, status)

            # Refresh tabel
            self.loadDataPengiriman()

            # Kosongkan form
            self.resetFormPengiriman()

            QMessageBox.information(self, "Berhasil", "Data pengiriman berhasil dirubah.")

    # ============ HAPUS ============
    def aksiHapusPengiriman(self):
        idpeng = self.ui_Pengiriman.txtIdPengiriman.text().strip()
        if idpeng == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus terlebih dahulu!")
            return

        # Konfirmasi penghapusan
        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus data pengiriman dengan ID '{idpeng}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            # Hapus data dari database
            self.aksiPengiriman.hapusPengiriman(idpeng)

            # Refresh tabel
            self.loadDataPengiriman()

            # Mengosongkan Form Input
            self.resetFormPengiriman()

            QMessageBox.information(self, "Berhasil", f"Data pengiriman dengan ID '{idpeng}' berhasil dihapus.")

    def loadDataPengiriman(self, data=None):
        # Jika tidak ada data dikirim, ambil semua data dari database
        if data is None:
            data = self.aksiPengiriman.tampilPengiriman()

        tabel = self.ui_Pengiriman.TabelPengiriman
        tabel.setRowCount(0)

        # Mapping ID Konsumen → Nama Konsumen
        konsumen_dict = {row[0]: row[1] for row in self.aksiKonsumen.tampilKonsumen()}

        # Mapping ID Pemesanan → ID Konsumen
        pemesanan_dict = {row[0]: row[1] for row in self.aksiPemesanan.tampilPemesanan()}

        # Set kolom tabel
        tabel.setColumnCount(8)
        tabel.setHorizontalHeaderLabels([
            "ID Pengiriman", "ID Pemesanan", "Nama Konsumen", "Tanggal Kirim",
            "Jumlah Kirim", "Kendaraan", "Sopir", "Status"
        ])

        # Isi data ke tabel
        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)

            id_pengiriman = row_data[0]
            id_pemesanan = row_data[1]
            tanggal_kirim = row_data[2]
            jumlah_kirim = row_data[3]
            kendaraan = row_data[4]
            sopir = row_data[5]
            status = row_data[6]

            # Ambil ID konsumen dari id_pemesanan
            id_konsumen = pemesanan_dict.get(id_pemesanan)
            nama_konsumen = konsumen_dict.get(id_konsumen, "Tidak Diketahui")

            # Susun isi tabel
            row_items = [
                id_pengiriman,
                id_pemesanan,
                nama_konsumen,
                tanggal_kirim,
                jumlah_kirim,
                kendaraan,
                sopir,
                status
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

    # ============ TAMPILKAN DATA KE FORM PENGIRIMAN ============
    def tampilDataKeFormPengiriman(self, row, column):
        tabel = self.ui_Pengiriman.TabelPengiriman

        # Ambil data dari tabel tampilan
        id_pengiriman = tabel.item(row, 0).text()
        id_pemesanan = tabel.item(row, 1).text()
        nama_konsumen = tabel.item(row, 2).text()
        tanggal_kirim = tabel.item(row, 3).text()
        jumlah_kirim = tabel.item(row, 4).text()
        kendaraan = tabel.item(row, 5).text()
        sopir = tabel.item(row, 6).text()
        status = tabel.item(row, 7).text()

        # Masukkan data ke form input
        self.ui_Pengiriman.txtIdPengiriman.setText(id_pengiriman)
        self.ui_Pengiriman.txtJumlahKirim.setText(jumlah_kirim)
        self.ui_Pengiriman.txtKendaraan.setText(kendaraan)
        self.ui_Pengiriman.txtSopir.setText(sopir)

        # ==== Atur tanggal ke QDateEdit ====
        qdate = QDate.fromString(tanggal_kirim, "yyyy-MM-dd")
        if qdate.isValid():
            self.ui_Pengiriman.datePengiriman.setDate(qdate)

        # ==== Atur ComboBox Pemesanan ====
        combo = self.ui_Pengiriman.cbPemesanan
        index = combo.findData(id_pemesanan)  # cocokkan berdasarkan data (id)
        if index != -1:
            combo.setCurrentIndex(index)
        else:
            combo.setCurrentIndex(0)  # fallback ke "Pilih Pemesanan"

        # ==== Atur ComboBox Status ====
        index_status = self.ui_Pengiriman.cbStatusPengiriman.findText(status, Qt.MatchFixedString)
        if index_status >= 0:
            self.ui_Pengiriman.cbStatusPengiriman.setCurrentIndex(index_status)

    # ============ LOAD PEMESANAN ============
    def loadPemesananKeCombo(self):
        data_pemesanan = self.aksiPemesanan.tampilPemesanan()
        data_konsumen = {row[0]: row[1] for row in self.aksiKonsumen.tampilKonsumen()}

        self.ui_Pengiriman.cbPemesanan.clear()

        # Tambahkan teks awal di ComboBox
        self.ui_Pengiriman.cbPemesanan.addItem("Pilih Pemesanan", None)

        # Tampilkan daftar Pemesanan + Nama Konsumen
        for row in data_pemesanan:
            id_pemesanan = row[0]
            id_konsumen = row[1]
            nama_konsumen = data_konsumen.get(id_konsumen, "Tidak Diketahui")

            tampil_combo = f"{id_pemesanan} - {nama_konsumen}"
            self.ui_Pengiriman.cbPemesanan.addItem(tampil_combo, id_pemesanan)

        # Atur posisi awal
        self.ui_Pengiriman.cbPemesanan.setCurrentIndex(0)

    def aksiCariPengiriman(self):
        nama = self.ui_Pengiriman.editCari.text().strip()
        if nama == "":
            # Jika kolom cari kosong, tampilkan semua data
            data = self.aksiPengiriman.tampilPengiriman()
        else:
            # Jika ada teks, filter berdasarkan nama konsumen
            data = self.aksiPengiriman.filterPengiriman(nama)
        # Update tabel dengan data yang difilter
        self.loadDataPengiriman(data)

    # ============ RESET FORM ============
    def resetFormPengiriman(self):
        self.ui_Pengiriman.txtIdPengiriman.clear()
        self.ui_Pengiriman.txtJumlahKirim.clear()
        self.ui_Pengiriman.txtKendaraan.clear()
        self.ui_Pengiriman.txtSopir.clear()
        self.ui_Pengiriman.datePengiriman.setDate(QtCore.QDate.currentDate())
        self.ui_Pengiriman.cbPemesanan.setCurrentIndex(0)
        self.ui_Pengiriman.cbStatusPengiriman.setCurrentIndex(0)
