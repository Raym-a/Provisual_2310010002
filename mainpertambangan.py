# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from konsumen import konsumen
from pemesanan import pemesanan
from produksi import produksi
from pengiriman import pengiriman


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('form.ui')
        filenya.open(QFile.ReadOnly)

        muatFile = QUiLoader()
        self.formMenu = muatFile.load(filenya,self)
        self.resize(self.formMenu.size())

        # Coding untuk Menampilkan Form Menu
        self.setMenuBar(self.formMenu.menuBar())

        # Codingan ini lanjutan dari Diatas untuk Menyambungkan Setiap Form menu ke Form Menu Bar
        self.formMenu.actionData_Konsumen.triggered.connect(self.bukaformKonsumen)
        self.formMenu.actionData_Pemesanan.triggered.connect(self.bukaformPemesanan)
        self.formMenu.actionData_Produksi.triggered.connect(self.bukaformProduksi)
        self.formMenu.actionData_Pengiriman.triggered.connect(self.bukaformPengiriman)

        # Codingan Untuk Membuka Menu Konsumen
    def bukaformKonsumen(self):
            self.tampil = konsumen()
            self.tampil.show()

        # Codingan Untuk Membuka Menu Pemesanan
    def bukaformPemesanan(self):
            self.tampil = pemesanan()
            self.tampil.show()

        # Codingan Untuk Membuka Menu Produksi
    def bukaformProduksi(self):
            self.tampil = produksi()
            self.tampil.show()

        # Codingan Untuk Membuka Menu Produksi
    def bukaformPengiriman(self):
        self.tampil = pengiriman()
        self.tampil.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
