# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainPertambangan(object):
    def setupUi(self, MainPertambangan):
        if not MainPertambangan.objectName():
            MainPertambangan.setObjectName(u"MainPertambangan")
        MainPertambangan.resize(800, 600)
        self.actionData_Konsumen = QAction(MainPertambangan)
        self.actionData_Konsumen.setObjectName(u"actionData_Konsumen")
        self.actionData_Pemesanan = QAction(MainPertambangan)
        self.actionData_Pemesanan.setObjectName(u"actionData_Pemesanan")
        self.actionData_Produksi = QAction(MainPertambangan)
        self.actionData_Produksi.setObjectName(u"actionData_Produksi")
        self.actionData_Pengiriman = QAction(MainPertambangan)
        self.actionData_Pengiriman.setObjectName(u"actionData_Pengiriman")
        self.centralwidget = QWidget(MainPertambangan)
        self.centralwidget.setObjectName(u"centralwidget")
        MainPertambangan.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainPertambangan)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuHalaman_Utama = QMenu(self.menubar)
        self.menuHalaman_Utama.setObjectName(u"menuHalaman_Utama")
        MainPertambangan.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainPertambangan)
        self.statusbar.setObjectName(u"statusbar")
        MainPertambangan.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman_Utama.menuAction())
        self.menuHalaman_Utama.addAction(self.actionData_Konsumen)
        self.menuHalaman_Utama.addAction(self.actionData_Pemesanan)
        self.menuHalaman_Utama.addAction(self.actionData_Produksi)
        self.menuHalaman_Utama.addAction(self.actionData_Pengiriman)

        self.retranslateUi(MainPertambangan)

        QMetaObject.connectSlotsByName(MainPertambangan)
    # setupUi

    def retranslateUi(self, MainPertambangan):
        MainPertambangan.setWindowTitle(QCoreApplication.translate("MainPertambangan", u"MainPertambangan", None))
        self.actionData_Konsumen.setText(QCoreApplication.translate("MainPertambangan", u"Data Konsumen", None))
        self.actionData_Pemesanan.setText(QCoreApplication.translate("MainPertambangan", u"Data Pemesanan", None))
        self.actionData_Produksi.setText(QCoreApplication.translate("MainPertambangan", u"Data Produksi", None))
        self.actionData_Pengiriman.setText(QCoreApplication.translate("MainPertambangan", u"Data Pengiriman", None))
        self.menuHalaman_Utama.setTitle(QCoreApplication.translate("MainPertambangan", u"Halaman Utama", None))
    # retranslateUi

