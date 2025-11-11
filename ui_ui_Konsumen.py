# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Konsumen.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_FormKonsumen(object):
    def setupUi(self, FormKonsumen):
        if not FormKonsumen.objectName():
            FormKonsumen.setObjectName(u"FormKonsumen")
        FormKonsumen.resize(600, 650)
        self.verticalLayout = QVBoxLayout(FormKonsumen)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.labelJudul = QLabel(FormKonsumen)
        self.labelJudul.setObjectName(u"labelJudul")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(14)
        font.setBold(True)
        self.labelJudul.setFont(font)
        self.labelJudul.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelJudul)

        self.groupBoxInput = QGroupBox(FormKonsumen)
        self.groupBoxInput.setObjectName(u"groupBoxInput")
        self.formLayout = QFormLayout(self.groupBoxInput)
        self.formLayout.setSpacing(15)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.iDKonsumenLabel = QLabel(self.groupBoxInput)
        self.iDKonsumenLabel.setObjectName(u"iDKonsumenLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDKonsumenLabel)

        self.txtIdKonsumen = QLineEdit(self.groupBoxInput)
        self.txtIdKonsumen.setObjectName(u"txtIdKonsumen")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtIdKonsumen)

        self.namaPerusahaanLabel = QLabel(self.groupBoxInput)
        self.namaPerusahaanLabel.setObjectName(u"namaPerusahaanLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPerusahaanLabel)

        self.txtNamaPerusahaan = QLineEdit(self.groupBoxInput)
        self.txtNamaPerusahaan.setObjectName(u"txtNamaPerusahaan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNamaPerusahaan)

        self.alamatLabel = QLabel(self.groupBoxInput)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.txtAlamat = QLineEdit(self.groupBoxInput)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtAlamat)

        self.kontakLabel = QLabel(self.groupBoxInput)
        self.kontakLabel.setObjectName(u"kontakLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kontakLabel)

        self.txtKontak = QLineEdit(self.groupBoxInput)
        self.txtKontak.setObjectName(u"txtKontak")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtKontak)


        self.verticalLayout.addWidget(self.groupBoxInput)

        self.horizontalLayoutButtons = QHBoxLayout()
        self.horizontalLayoutButtons.setSpacing(15)
        self.horizontalLayoutButtons.setObjectName(u"horizontalLayoutButtons")
        self.btnTambahKonsumen = QPushButton(FormKonsumen)
        self.btnTambahKonsumen.setObjectName(u"btnTambahKonsumen")
        self.btnTambahKonsumen.setMinimumSize(QSize(100, 35))

        self.horizontalLayoutButtons.addWidget(self.btnTambahKonsumen)

        self.btnEditKonsumen = QPushButton(FormKonsumen)
        self.btnEditKonsumen.setObjectName(u"btnEditKonsumen")
        self.btnEditKonsumen.setMinimumSize(QSize(100, 35))

        self.horizontalLayoutButtons.addWidget(self.btnEditKonsumen)

        self.btnHapusKonsumen = QPushButton(FormKonsumen)
        self.btnHapusKonsumen.setObjectName(u"btnHapusKonsumen")
        self.btnHapusKonsumen.setMinimumSize(QSize(100, 35))

        self.horizontalLayoutButtons.addWidget(self.btnHapusKonsumen)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutButtons.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayoutButtons)

        self.horizontalLayoutCari = QHBoxLayout()
        self.horizontalLayoutCari.setSpacing(10)
        self.horizontalLayoutCari.setObjectName(u"horizontalLayoutCari")
        self.labelCari = QLabel(FormKonsumen)
        self.labelCari.setObjectName(u"labelCari")

        self.horizontalLayoutCari.addWidget(self.labelCari)

        self.editCari = QLineEdit(FormKonsumen)
        self.editCari.setObjectName(u"editCari")

        self.horizontalLayoutCari.addWidget(self.editCari)


        self.verticalLayout.addLayout(self.horizontalLayoutCari)

        self.TabelKonsumen = QTableWidget(FormKonsumen)
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
        self.TabelKonsumen.setMinimumSize(QSize(0, 200))
        self.TabelKonsumen.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.TabelKonsumen)


        self.retranslateUi(FormKonsumen)

        QMetaObject.connectSlotsByName(FormKonsumen)
    # setupUi

    def retranslateUi(self, FormKonsumen):
        FormKonsumen.setWindowTitle(QCoreApplication.translate("FormKonsumen", u"Data Konsumen", None))
        FormKonsumen.setStyleSheet(QCoreApplication.translate("FormKonsumen", u"QWidget { background-color: #f5f5f5; }\n"
"QLabel { color: #333; font-weight: bold; }\n"
"QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 4px; }\n"
"QPushButton { background-color: #4CAF50; color: white; border: none; border-radius: 4px; padding: 8px 16px; font-weight: bold; }\n"
"QPushButton:hover { background-color: #45a049; }\n"
"QTableWidget { border: 1px solid #ccc; gridline-color: #ddd; }", None))
        self.labelJudul.setText(QCoreApplication.translate("FormKonsumen", u"DATA KONSUMEN", None))
        self.groupBoxInput.setTitle(QCoreApplication.translate("FormKonsumen", u"Informasi Konsumen", None))
        self.iDKonsumenLabel.setText(QCoreApplication.translate("FormKonsumen", u"ID Konsumen:", None))
        self.namaPerusahaanLabel.setText(QCoreApplication.translate("FormKonsumen", u"Nama Perusahaan:", None))
        self.alamatLabel.setText(QCoreApplication.translate("FormKonsumen", u"Alamat:", None))
        self.kontakLabel.setText(QCoreApplication.translate("FormKonsumen", u"Kontak:", None))
        self.btnTambahKonsumen.setText(QCoreApplication.translate("FormKonsumen", u"Simpan", None))
        self.btnEditKonsumen.setText(QCoreApplication.translate("FormKonsumen", u"Edit", None))
        self.btnHapusKonsumen.setText(QCoreApplication.translate("FormKonsumen", u"Hapus", None))
        self.labelCari.setText(QCoreApplication.translate("FormKonsumen", u"Cari:", None))
        ___qtablewidgetitem = self.TabelKonsumen.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormKonsumen", u"ID Konsumen", None));
        ___qtablewidgetitem1 = self.TabelKonsumen.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormKonsumen", u"Nama Perusahaan", None));
        ___qtablewidgetitem2 = self.TabelKonsumen.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormKonsumen", u"Alamat", None));
        ___qtablewidgetitem3 = self.TabelKonsumen.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormKonsumen", u"Kontak", None));
    # retranslateUi

