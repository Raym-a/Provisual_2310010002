from PySide6.QtWidgets import QApplication, QWidget, QHeaderView, QMessageBox
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets


# Import File CRUD
from crud_Konsumen import crudKonsumen


class konsumen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("ui_Konsumen.ui")
        filenya.open(QFile.ReadOnly)

        muatFile = QUiLoader()
        self.ui_Konsumen = muatFile.load(filenya, self)

        # === Inisialisasi CRUD ===
        self.aksiCrud = crudKonsumen()

        # === Load Data Awal ke Tabel ===
        self.loadDataKonsumen()

        # === Event Klik Tabel untuk isi form otomatis ===
        self.ui_Konsumen.TabelKonsumen.cellClicked.connect(self.tampilDataKeForm)

        # === Header Tengah ===
        self.ui_Konsumen.TabelKonsumen.horizontalHeader().setDefaultAlignment(
            Qt.AlignCenter
        )

        # === Koneksi Button CRUD ===
        self.ui_Konsumen.btnTambahKonsumen.clicked.connect(self.aksiSimpanKonsumen)
        self.ui_Konsumen.btnEditKonsumen.clicked.connect(self.aksiEditKonsumen)
        self.ui_Konsumen.btnHapusKonsumen.clicked.connect(self.aksiHapusKonsumen)

        # === Koneksi Fitur Pencarian ===
        self.ui_Konsumen.editCari.textChanged.connect(self.aksiCariKonsumen)

        ## Coding Untuk Rumus / Cara Button Bekerja

        # ============ SIMPAN ============

    def aksiSimpanKonsumen(self):
        if not self.ui_Konsumen.txtIdKonsumen.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Konsumen tidak boleh kosong!")
            return
        elif not self.ui_Konsumen.txtNamaPerusahaan.text().strip():
            QMessageBox.warning(
                self, "Peringatan", "Nama Perusahaan tidak boleh kosong!"
            )
            return
        elif not self.ui_Konsumen.txtAlamat.text().strip():
            QMessageBox.warning(self, "Peringatan", "Alamat tidak boleh kosong!")
            return
        elif not self.ui_Konsumen.txtKontak.text().strip():
            QMessageBox.warning(self, "Peringatan", "Kontak tidak boleh kosong!")
            return
        else:
            id = self.ui_Konsumen.txtIdKonsumen.text()
            nama = self.ui_Konsumen.txtNamaPerusahaan.text()
            alamat = self.ui_Konsumen.txtAlamat.text()
            kontak = self.ui_Konsumen.txtKontak.text()

            # Coding untuk Mengirim/menimpan  data ke database
            self.aksiCrud.simpanKonsumen(id, nama, alamat, kontak)

            # Refresh tabel setelah data berhasil disimpan
            self.loadDataKonsumen()

            # Kosongkan form input
            self.aksiResetKonsumen()

            QMessageBox.information(
                self, "Berhasil", "Data konsumen berhasil disimpan."
            )

    # ============ EDIT ============
    def aksiEditKonsumen(self):
        if not self.ui_Konsumen.txtIdKonsumen.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Konsumen tidak boleh kosong!")
            return
        elif not self.ui_Konsumen.txtNamaPerusahaan.text().strip():
            QMessageBox.warning(
                self, "Peringatan", "Nama Perusahaan tidak boleh kosong!"
            )
            return
        elif not self.ui_Konsumen.txtAlamat.text().strip():
            QMessageBox.warning(self, "Peringatan", "Alamat tidak boleh kosong!")
            return
        elif not self.ui_Konsumen.txtKontak.text().strip():
            QMessageBox.warning(self, "Peringatan", "Kontak tidak boleh kosong!")
            return
        else:
            id = self.ui_Konsumen.txtIdKonsumen.text()
            nama = self.ui_Konsumen.txtNamaPerusahaan.text()
            alamat = self.ui_Konsumen.txtAlamat.text()
            kontak = self.ui_Konsumen.txtKontak.text()

            # Coding untuk Mengirim/menimpan  data ke database
            self.aksiCrud.editKonsumen(id, nama, alamat, kontak)

            # Refresh tabel setelah data berhasil disimpan
            self.loadDataKonsumen()

            # Kosongkan form input
            self.aksiResetKonsumen()

            QMessageBox.information(self, "Berhasil", "Data konsumen berhasil terubah.")

    # ============ HAPUS ============
    def aksiHapusKonsumen(self):
        pesan = self.ui_Konsumen.txtIdKonsumen.text()
        if pesan == "":
            QMessageBox.warning(
                self, "Peringatan", "Pilih data yang ingin dihapus terlebih dahulu!"
            )
            return

        # Konfirmasi penghapusan
        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Apakah Anda yakin ingin menghapus data konsumen dengan ID '{pesan}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if konfirmasi == QMessageBox.Yes:
            try:
                self.aksiCrud.hapusKonsumen(pesan)
                self.loadDataKonsumen()

                # Kosongkan form input
                self.aksiResetKonsumen()

                QMessageBox.information(
                    self,
                    "Berhasil",
                    f"Data konsumen dengan ID '{pesan}' berhasil dihapus.",
                )
            except Exception as e:
                QMessageBox.critical(
                    self, "Kesalahan", f"Gagal menghapus data!\n\n{str(e)}"
                )

    ## UNTUK Menampilkan Seluruh Data pada Table Konsumen Setelah diambil dari file
    ## crudKonsumen def tampilKonsumen(self): Dan Juga untuk Codingan Membuka Menu Konsumen

    def loadDataKonsumen(self):
        data = self.aksiCrud.tampilKonsumen()
        tabel = self.ui_Konsumen.TabelKonsumen
        tabel.setRowCount(0)  # Hapus semua baris sebelum menampilkan ulang

        # Kosongkan tabel dulu
        tabel.setColumnCount(4)
        tabel.setHorizontalHeaderLabels(
            ["ID Konsumen", "Nama Perusahaan", "Alamat", "Kontak"]
        )

        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)
            for column_number, cell_data in enumerate(row_data):
                tabel.setItem(
                    row_number,
                    column_number,
                    QtWidgets.QTableWidgetItem(str(cell_data)),
                )

        # Header tabel di tengah dan kolom sama lebar
        header = tabel.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignCenter)
        header.setStretchLastSection(True)
        for i in range(4):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    # Rumus Codingan Agar Klik Otomatis muncul di form input (Baris ke - 23) Berfungsi
    def tampilDataKeForm(self, row, column):
        tabel = self.ui_Konsumen.TabelKonsumen
        id_konsumen = tabel.item(row, 0).text()
        nama_perusahaan = tabel.item(row, 1).text()
        alamat = tabel.item(row, 2).text()
        kontak = tabel.item(row, 3).text()
        self.ui_Konsumen.txtIdKonsumen.setText(id_konsumen)
        self.ui_Konsumen.txtNamaPerusahaan.setText(nama_perusahaan)
        self.ui_Konsumen.txtAlamat.setText(alamat)
        self.ui_Konsumen.txtKontak.setText(kontak)

    def aksiCariKonsumen(self):
        nama = self.ui_Konsumen.editCari.text().strip()

        if nama == "":
            # Jika kolom cari kosong, tampilkan semua data
            data = self.aksiCrud.tampilKonsumen()
        else:
            # Jika ada teks, filter berdasarkan nama
            data = self.aksiCrud.filterKonsumen(nama)

        tabel = self.ui_Konsumen.TabelKonsumen
        tabel.setRowCount(0)
        tabel.setColumnCount(4)
        tabel.setHorizontalHeaderLabels(
            ["ID Konsumen", "Nama Perusahaan", "Alamat", "Kontak"]
        )

        for row_number, row_data in enumerate(data):
            tabel.insertRow(row_number)
            for column_number, cell_data in enumerate(row_data):
                tabel.setItem(
                    row_number,
                    column_number,
                    QtWidgets.QTableWidgetItem(str(cell_data)),
                )

    # ============ RESET FORM ============
    def aksiResetKonsumen(self):
        self.ui_Konsumen.txtIdKonsumen.clear()
        self.ui_Konsumen.txtNamaPerusahaan.clear()
        self.ui_Konsumen.txtAlamat.clear()
        self.ui_Konsumen.txtKontak.clear()
