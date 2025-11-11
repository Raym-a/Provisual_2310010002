# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Pengiriman.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txtIdPengiriman = QLineEdit(self.groupBox)
        self.txtIdPengiriman.setObjectName(u"txtIdPengiriman")

        self.gridLayout.addWidget(self.txtIdPengiriman, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.cbPemesanan = QComboBox(self.groupBox)
        self.cbPemesanan.setObjectName(u"cbPemesanan")

        self.gridLayout.addWidget(self.cbPemesanan, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.datePengiriman = QDateEdit(self.groupBox)
        self.datePengiriman.setObjectName(u"datePengiriman")
        self.datePengiriman.setCalendarPopup(True)

        self.gridLayout.addWidget(self.datePengiriman, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.txtJumlahKirim = QLineEdit(self.groupBox)
        self.txtJumlahKirim.setObjectName(u"txtJumlahKirim")

        self.gridLayout.addWidget(self.txtJumlahKirim, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.txtKendaraan = QLineEdit(self.groupBox)
        self.txtKendaraan.setObjectName(u"txtKendaraan")

        self.gridLayout.addWidget(self.txtKendaraan, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.txtSopir = QLineEdit(self.groupBox)
        self.txtSopir.setObjectName(u"txtSopir")

        self.gridLayout.addWidget(self.txtSopir, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.cbStatusPengiriman = QComboBox(self.groupBox)
        self.cbStatusPengiriman.addItem("")
        self.cbStatusPengiriman.addItem("")
        self.cbStatusPengiriman.setObjectName(u"cbStatusPengiriman")

        self.gridLayout.addWidget(self.cbStatusPengiriman, 6, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnTambahPengiriman = QPushButton(Form)
        self.btnTambahPengiriman.setObjectName(u"btnTambahPengiriman")

        self.horizontalLayout.addWidget(self.btnTambahPengiriman)

        self.btnEditPengiriman = QPushButton(Form)
        self.btnEditPengiriman.setObjectName(u"btnEditPengiriman")

        self.horizontalLayout.addWidget(self.btnEditPengiriman)

        self.btnHapusPengiriman = QPushButton(Form)
        self.btnHapusPengiriman.setObjectName(u"btnHapusPengiriman")

        self.horizontalLayout.addWidget(self.btnHapusPengiriman)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")

        self.horizontalLayout.addWidget(self.editCari)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.TabelPengiriman = QTableWidget(Form)
        self.TabelPengiriman.setObjectName(u"TabelPengiriman")
        self.TabelPengiriman.setColumnCount(8)
        self.TabelPengiriman.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout.addWidget(self.TabelPengiriman)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Manajemen Pengiriman", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Form Input Pengiriman", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Pengiriman:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pemesanan:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tanggal Kirim:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Jumlah Kirim:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Kendaraan:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Sopir:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.cbStatusPengiriman.setItemText(0, QCoreApplication.translate("Form", u"dikirim", None))
        self.cbStatusPengiriman.setItemText(1, QCoreApplication.translate("Form", u"selesai", None))

        self.btnTambahPengiriman.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.btnEditPengiriman.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.btnHapusPengiriman.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Cari Konsumen:", None))
    # retranslateUi

