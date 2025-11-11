# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Pemesanan.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_FormPemesanan(object):
    def setupUi(self, FormPemesanan):
        if not FormPemesanan.objectName():
            FormPemesanan.setObjectName(u"FormPemesanan")
        FormPemesanan.resize(1106, 465)
        self.btnEditPemesanan = QPushButton(FormPemesanan)
        self.btnEditPemesanan.setObjectName(u"btnEditPemesanan")
        self.btnEditPemesanan.setGeometry(QRect(230, 320, 90, 41))
        self.formLayoutWidget = QWidget(FormPemesanan)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 60, 501, 246))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.namaPemesananLabel = QLabel(self.formLayoutWidget)
        self.namaPemesananLabel.setObjectName(u"namaPemesananLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPemesananLabel)

        self.cbKonsumen = QComboBox(self.formLayoutWidget)
        self.cbKonsumen.setObjectName(u"cbKonsumen")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cbKonsumen)

        self.tanggalPesananLabel = QLabel(self.formLayoutWidget)
        self.tanggalPesananLabel.setObjectName(u"tanggalPesananLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggalPesananLabel)

        self.datePemesanan = QDateEdit(self.formLayoutWidget)
        self.datePemesanan.setObjectName(u"datePemesanan")
        self.datePemesanan.setCalendarPopup(False)
        self.datePemesanan.setDate(QDate(2000, 1, 2))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.datePemesanan)

        self.totalHargaLabel = QLabel(self.formLayoutWidget)
        self.totalHargaLabel.setObjectName(u"totalHargaLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.totalHargaLabel)

        self.txtTotalHarga = QLineEdit(self.formLayoutWidget)
        self.txtTotalHarga.setObjectName(u"txtTotalHarga")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtTotalHarga)

        self.statusPemesananLabel = QLabel(self.formLayoutWidget)
        self.statusPemesananLabel.setObjectName(u"statusPemesananLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.statusPemesananLabel)

        self.cbStatusPemesanan = QComboBox(self.formLayoutWidget)
        self.cbStatusPemesanan.addItem("")
        self.cbStatusPemesanan.addItem("")
        self.cbStatusPemesanan.addItem("")
        self.cbStatusPemesanan.setObjectName(u"cbStatusPemesanan")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cbStatusPemesanan)

        self.txtIdPemesanan = QLineEdit(self.formLayoutWidget)
        self.txtIdPemesanan.setObjectName(u"txtIdPemesanan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtIdPemesanan)

        self.iDPemesananLabel = QLabel(self.formLayoutWidget)
        self.iDPemesananLabel.setObjectName(u"iDPemesananLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPemesananLabel)

        self.produkDipesanLabel = QLabel(self.formLayoutWidget)
        self.produkDipesanLabel.setObjectName(u"produkDipesanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.produkDipesanLabel)

        self.txtProdukDipesan = QLineEdit(self.formLayoutWidget)
        self.txtProdukDipesan.setObjectName(u"txtProdukDipesan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtProdukDipesan)

        self.btnTambahPemesanan = QPushButton(FormPemesanan)
        self.btnTambahPemesanan.setObjectName(u"btnTambahPemesanan")
        self.btnTambahPemesanan.setGeometry(QRect(130, 320, 90, 41))
        self.TabelPemesanan = QTableWidget(FormPemesanan)
        if (self.TabelPemesanan.columnCount() < 6):
            self.TabelPemesanan.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.TabelPemesanan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TabelPemesanan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TabelPemesanan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TabelPemesanan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TabelPemesanan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TabelPemesanan.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.TabelPemesanan.setObjectName(u"TabelPemesanan")
        self.TabelPemesanan.setGeometry(QRect(560, 60, 501, 361))
        self.label = QLabel(FormPemesanan)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 10, 231, 31))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.btnHapusPemesanan = QPushButton(FormPemesanan)
        self.btnHapusPemesanan.setObjectName(u"btnHapusPemesanan")
        self.btnHapusPemesanan.setGeometry(QRect(330, 320, 90, 41))
        self.editCari = QLineEdit(FormPemesanan)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(30, 380, 491, 41))

        self.retranslateUi(FormPemesanan)

        QMetaObject.connectSlotsByName(FormPemesanan)
    # setupUi

    def retranslateUi(self, FormPemesanan):
        FormPemesanan.setWindowTitle(QCoreApplication.translate("FormPemesanan", u"Form", None))
        self.btnEditPemesanan.setText(QCoreApplication.translate("FormPemesanan", u"Edit", None))
        self.namaPemesananLabel.setText(QCoreApplication.translate("FormPemesanan", u"Nama Pemesanan", None))
        self.tanggalPesananLabel.setText(QCoreApplication.translate("FormPemesanan", u"Tanggal Pesanan", None))
        self.totalHargaLabel.setText(QCoreApplication.translate("FormPemesanan", u"Total Harga", None))
        self.statusPemesananLabel.setText(QCoreApplication.translate("FormPemesanan", u"Status Pemesanan", None))
        self.cbStatusPemesanan.setItemText(0, QCoreApplication.translate("FormPemesanan", u"Pilih Status", None))
        self.cbStatusPemesanan.setItemText(1, QCoreApplication.translate("FormPemesanan", u"Proses", None))
        self.cbStatusPemesanan.setItemText(2, QCoreApplication.translate("FormPemesanan", u"Selesai", None))

        self.iDPemesananLabel.setText(QCoreApplication.translate("FormPemesanan", u"ID Pemesanan", None))
        self.produkDipesanLabel.setText(QCoreApplication.translate("FormPemesanan", u"Produk Dipesan", None))
        self.btnTambahPemesanan.setText(QCoreApplication.translate("FormPemesanan", u"Simpan", None))
        ___qtablewidgetitem = self.TabelPemesanan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormPemesanan", u"ID Pemesanan", None));
        ___qtablewidgetitem1 = self.TabelPemesanan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormPemesanan", u"Nama Pemesanan", None));
        ___qtablewidgetitem2 = self.TabelPemesanan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormPemesanan", u"Produk Dipesan", None));
        ___qtablewidgetitem3 = self.TabelPemesanan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormPemesanan", u"Tanggal Pesanan", None));
        ___qtablewidgetitem4 = self.TabelPemesanan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormPemesanan", u"Total Harga", None));
        ___qtablewidgetitem5 = self.TabelPemesanan.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormPemesanan", u"Status Pemesanan", None));
        self.label.setText(QCoreApplication.translate("FormPemesanan", u"DATA PEMESANAN", None))
        self.btnHapusPemesanan.setText(QCoreApplication.translate("FormPemesanan", u"Hapus", None))
    # retranslateUi

