# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Produksi.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 619)
        self.btnHapusProduksi = QPushButton(Form)
        self.btnHapusProduksi.setObjectName(u"btnHapusProduksi")
        self.btnHapusProduksi.setGeometry(QRect(330, 280, 90, 41))
        self.TabelProduksi = QTableWidget(Form)
        if (self.TabelProduksi.columnCount() < 5):
            self.TabelProduksi.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.TabelProduksi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TabelProduksi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TabelProduksi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TabelProduksi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TabelProduksi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.TabelProduksi.setObjectName(u"TabelProduksi")
        self.TabelProduksi.setGeometry(QRect(20, 402, 511, 192))
        self.btnEditProduksi = QPushButton(Form)
        self.btnEditProduksi.setObjectName(u"btnEditProduksi")
        self.btnEditProduksi.setGeometry(QRect(230, 280, 90, 41))
        self.btnTambahProduksi = QPushButton(Form)
        self.btnTambahProduksi.setObjectName(u"btnTambahProduksi")
        self.btnTambahProduksi.setGeometry(QRect(130, 280, 90, 41))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 10, 211, 31))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 41, 511, 228))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.iDProduksiLabel = QLabel(self.formLayoutWidget)
        self.iDProduksiLabel.setObjectName(u"iDProduksiLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDProduksiLabel)

        self.txtIdProduksi = QLineEdit(self.formLayoutWidget)
        self.txtIdProduksi.setObjectName(u"txtIdProduksi")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtIdProduksi)

        self.iDPemesananLabel = QLabel(self.formLayoutWidget)
        self.iDPemesananLabel.setObjectName(u"iDPemesananLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.iDPemesananLabel)

        self.cbPemesanan = QComboBox(self.formLayoutWidget)
        self.cbPemesanan.setObjectName(u"cbPemesanan")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cbPemesanan)

        self.tanggalProduksiLabel = QLabel(self.formLayoutWidget)
        self.tanggalProduksiLabel.setObjectName(u"tanggalProduksiLabel")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggalProduksiLabel)

        self.dateProduksi = QDateEdit(self.formLayoutWidget)
        self.dateProduksi.setObjectName(u"dateProduksi")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateProduksi)

        self.jumlahProduksiLabel = QLabel(self.formLayoutWidget)
        self.jumlahProduksiLabel.setObjectName(u"jumlahProduksiLabel")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jumlahProduksiLabel)

        self.txtJumlahProduksi = QLineEdit(self.formLayoutWidget)
        self.txtJumlahProduksi.setObjectName(u"txtJumlahProduksi")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtJumlahProduksi)

        self.KeteranganLabel = QLabel(self.formLayoutWidget)
        self.KeteranganLabel.setObjectName(u"KeteranganLabel")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.KeteranganLabel)

        self.txtKeterangan = QTextEdit(self.formLayoutWidget)
        self.txtKeterangan.setObjectName(u"txtKeterangan")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtKeterangan)

        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(20, 340, 511, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnHapusProduksi.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.TabelProduksi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Produksi", None));
        ___qtablewidgetitem1 = self.TabelProduksi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID Pemesanan", None));
        ___qtablewidgetitem2 = self.TabelProduksi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal Produksi", None));
        ___qtablewidgetitem3 = self.TabelProduksi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jumlah Produksi", None));
        ___qtablewidgetitem4 = self.TabelProduksi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        self.btnEditProduksi.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.btnTambahProduksi.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.label.setText(QCoreApplication.translate("Form", u"DATA PRODUKSI", None))
        self.iDProduksiLabel.setText(QCoreApplication.translate("Form", u"ID Produksi", None))
        self.iDPemesananLabel.setText(QCoreApplication.translate("Form", u"ID Pemesanan", None))
        self.tanggalProduksiLabel.setText(QCoreApplication.translate("Form", u"Tanggal Produksi", None))
        self.jumlahProduksiLabel.setText(QCoreApplication.translate("Form", u"Jumlah Produksi", None))
        self.KeteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
    # retranslateUi

