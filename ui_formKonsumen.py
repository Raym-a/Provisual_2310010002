# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formKonsumen.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 550)
        Form.setAutoFillBackground(False)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 60, 511, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDKonsumenLabel = QLabel(self.formLayoutWidget)
        self.iDKonsumenLabel.setObjectName(u"iDKonsumenLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDKonsumenLabel)

        self.txtIdKonsumen = QLineEdit(self.formLayoutWidget)
        self.txtIdKonsumen.setObjectName(u"txtIdKonsumen")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtIdKonsumen)

        self.namaPerusahaanLabel = QLabel(self.formLayoutWidget)
        self.namaPerusahaanLabel.setObjectName(u"namaPerusahaanLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPerusahaanLabel)

        self.txtNamaPerusahaan = QLineEdit(self.formLayoutWidget)
        self.txtNamaPerusahaan.setObjectName(u"txtNamaPerusahaan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNamaPerusahaan)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.txtAlamat = QLineEdit(self.formLayoutWidget)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtAlamat)

        self.kontakLabel = QLabel(self.formLayoutWidget)
        self.kontakLabel.setObjectName(u"kontakLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kontakLabel)

        self.txtKontak = QLineEdit(self.formLayoutWidget)
        self.txtKontak.setObjectName(u"txtKontak")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtKontak)

        self.btnTambahKonsumen = QPushButton(Form)
        self.btnTambahKonsumen.setObjectName(u"btnTambahKonsumen")
        self.btnTambahKonsumen.setGeometry(QRect(120, 218, 90, 41))
        self.btnEditKonsumen = QPushButton(Form)
        self.btnEditKonsumen.setObjectName(u"btnEditKonsumen")
        self.btnEditKonsumen.setGeometry(QRect(220, 218, 90, 41))
        self.btnHapusKonsumen = QPushButton(Form)
        self.btnHapusKonsumen.setObjectName(u"btnHapusKonsumen")
        self.btnHapusKonsumen.setGeometry(QRect(320, 218, 90, 41))
        self.TabelKonsumen = QTableWidget(Form)
        if (self.TabelKonsumen.columnCount() < 4):
            self.TabelKonsumen.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.TabelKonsumen.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TabelKonsumen.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TabelKonsumen.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TabelKonsumen.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.TabelKonsumen.setObjectName(u"TabelKonsumen")
        self.TabelKonsumen.setGeometry(QRect(20, 340, 511, 192))
        self.btnTambahKonsumen_2 = QPushButton(Form)
        self.btnTambahKonsumen_2.setObjectName(u"btnTambahKonsumen_2")
        self.btnTambahKonsumen_2.setGeometry(QRect(20, 270, 501, 41))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 19, 181, 31))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDKonsumenLabel.setText(QCoreApplication.translate("Form", u"ID Konsumen", None))
        self.namaPerusahaanLabel.setText(QCoreApplication.translate("Form", u"Nama Perusahaan", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.kontakLabel.setText(QCoreApplication.translate("Form", u"Kontak", None))
        self.btnTambahKonsumen.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnEditKonsumen.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.btnHapusKonsumen.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.TabelKonsumen.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Konsumen", None));
        ___qtablewidgetitem1 = self.TabelKonsumen.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Perusahaan", None));
        ___qtablewidgetitem2 = self.TabelKonsumen.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem3 = self.TabelKonsumen.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Kontak", None));
        self.btnTambahKonsumen_2.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.label.setText(QCoreApplication.translate("Form", u"DATA KONSUMEN", None))
    # retranslateUi

