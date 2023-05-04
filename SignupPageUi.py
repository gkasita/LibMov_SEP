# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignupPageUi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 400, 650))
        self.frame_2.setMinimumSize(QSize(400, 650))
        self.frame_2.setMaximumSize(QSize(400, 650))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.titleLB = QLabel(self.frame_2)
        self.titleLB.setObjectName(u"titleLB")
        self.titleLB.setGeometry(QRect(60, 200, 291, 41))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(24)
        font.setBold(True)
        self.titleLB.setFont(font)
        self.titleLB.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textLB = QLabel(self.frame_2)
        self.textLB.setObjectName(u"textLB")
        self.textLB.setGeometry(QRect(80, 260, 271, 41))
        font1 = QFont()
        font1.setFamilies([u"Heiti SC"])
        font1.setKerning(True)
        self.textLB.setFont(font1)
        self.textLB.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textLB.setLineWidth(1)
        self.textLB2 = QLabel(self.frame_2)
        self.textLB2.setObjectName(u"textLB2")
        self.textLB2.setGeometry(QRect(20, 300, 381, 31))
        self.textLB2.setFont(font1)
        self.textLB2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textLB2.setLineWidth(1)
        self.backBT = QPushButton(self.frame_2)
        self.backBT.setObjectName(u"backBT")
        self.backBT.setGeometry(QRect(120, 370, 161, 41))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(18)
        self.backBT.setFont(font2)
        self.backBT.setStyleSheet(u"background-color: rgb(131, 16, 16);\n"
"border-radius: 15px;")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(400, 0, 550, 650))
        self.frame.setMinimumSize(QSize(550, 650))
        self.frame.setMaximumSize(QSize(550, 650))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.usernameLED = QLineEdit(self.frame)
        self.usernameLED.setObjectName(u"usernameLED")
        self.usernameLED.setGeometry(QRect(120, 270, 301, 41))
        self.usernameLED.setAutoFillBackground(False)
        self.usernameLED.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.usernameLED.setFrame(True)
        self.signupBT = QPushButton(self.frame)
        self.signupBT.setObjectName(u"signupBT")
        self.signupBT.setGeometry(QRect(200, 520, 161, 41))
        self.signupBT.setFont(font2)
        self.signupBT.setStyleSheet(u"background-color: rgb(131, 16, 16);\n"
"border-radius: 15px;")
        self.passwordLED = QLineEdit(self.frame)
        self.passwordLED.setObjectName(u"passwordLED")
        self.passwordLED.setGeometry(QRect(120, 350, 301, 41))
        self.passwordLED.setAutoFillBackground(False)
        self.passwordLED.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.passwordLED.setFrame(True)
        self.cfpasswordLED = QLineEdit(self.frame)
        self.cfpasswordLED.setObjectName(u"cfpasswordLED")
        self.cfpasswordLED.setGeometry(QRect(120, 430, 301, 41))
        self.cfpasswordLED.setAutoFillBackground(False)
        self.cfpasswordLED.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.cfpasswordLED.setFrame(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 170, 181, 61))
        font3 = QFont()
        font3.setFamilies([u"Al Nile"])
        font3.setPointSize(40)
        font3.setBold(True)
        self.label.setFont(font3)
        self.errorLB = QLabel(self.frame)
        self.errorLB.setObjectName(u"errorLB")
        self.errorLB.setGeometry(QRect(120, 490, 311, 16))
        self.errorLB.setStyleSheet(u"color: rgb(229, 9, 20);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLB.setText(QCoreApplication.translate("Form", u"Thanks for joining us", None))
        self.textLB.setText(QCoreApplication.translate("Form", u"We can't wait for you to start exploring", None))
        self.textLB2.setText(QCoreApplication.translate("Form", u"our application and discovering all the amazing features!", None))
        self.backBT.setText(QCoreApplication.translate("Form", u"Back", None))
        self.usernameLED.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.signupBT.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.passwordLED.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.cfpasswordLED.setPlaceholderText(QCoreApplication.translate("Form", u"Confirmed Password", None))
        self.label.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.errorLB.setText("")
    # retranslateUi

