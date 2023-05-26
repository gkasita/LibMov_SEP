# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfilePageUi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
        Form.setSizeIncrement(QSize(300, 200))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.menu = QFrame(Form)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 100, 650))
        self.menu.setMinimumSize(QSize(100, 650))
        self.menu.setMaximumSize(QSize(100, 650))
        self.menu.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.logoutBT = QPushButton(self.menu)
        self.logoutBT.setObjectName(u"logoutBT")
        self.logoutBT.setGeometry(QRect(0, 580, 100, 50))
        self.logoutBT.setMinimumSize(QSize(100, 50))
        self.logoutBT.setMaximumSize(QSize(100, 50))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(15)
        font.setBold(True)
        self.logoutBT.setFont(font)
        self.logoutBT.setStyleSheet(u"color: rgb(131, 16, 16);")
        self.reviewBT = QPushButton(self.menu)
        self.reviewBT.setObjectName(u"reviewBT")
        self.reviewBT.setGeometry(QRect(0, 160, 100, 50))
        self.reviewBT.setMinimumSize(QSize(100, 50))
        self.reviewBT.setMaximumSize(QSize(100, 50))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(14)
        self.reviewBT.setFont(font1)
        self.reviewBT.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.watchBT = QPushButton(self.menu)
        self.watchBT.setObjectName(u"watchBT")
        self.watchBT.setGeometry(QRect(0, 210, 100, 50))
        self.watchBT.setMinimumSize(QSize(100, 50))
        self.watchBT.setMaximumSize(QSize(100, 50))
        self.watchBT.setFont(font1)
        self.watchBT.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.libmovBT = QPushButton(self.menu)
        self.libmovBT.setObjectName(u"libmovBT")
        self.libmovBT.setGeometry(QRect(0, 0, 100, 80))
        self.libmovBT.setMinimumSize(QSize(100, 80))
        self.libmovBT.setMaximumSize(QSize(100, 80))
        self.libmovBT.setFont(font)
        self.libmovBT.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(131, 16, 16);")
        self.profileBT = QPushButton(self.menu)
        self.profileBT.setObjectName(u"profileBT")
        self.profileBT.setGeometry(QRect(0, 110, 100, 50))
        self.profileBT.setMinimumSize(QSize(100, 50))
        self.profileBT.setMaximumSize(QSize(100, 50))
        self.profileBT.setFont(font1)
        self.profileBT.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(500, 200, 200, 50))
        self.button = QPushButton(Form)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(490, 260, 101, 24))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 330, 49, 16))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 330, 49, 16))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(780, 330, 61, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 370, 49, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(520, 370, 49, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(780, 370, 49, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logoutBT.setText(QCoreApplication.translate("Form", u"Log out", None))
        self.reviewBT.setText(QCoreApplication.translate("Form", u"Review", None))
        self.watchBT.setText(QCoreApplication.translate("Form", u"Watched", None))
        self.libmovBT.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.profileBT.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.label.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.button.setText(QCoreApplication.translate("Form", u"Chang Password", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Watched", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Watching", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Will Watch", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

