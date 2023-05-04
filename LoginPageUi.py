# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPageUi.ui'
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
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 550, 650))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(550, 650))
        self.frame.setMaximumSize(QSize(550, 650))
        self.frame.setLayoutDirection(Qt.LeftToRight)
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
        self.loginBT = QPushButton(self.frame)
        self.loginBT.setObjectName(u"loginBT")
        self.loginBT.setGeometry(QRect(200, 430, 161, 41))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(18)
        self.loginBT.setFont(font)
        self.loginBT.setStyleSheet(u"background-color: rgb(131, 16, 16);\n"
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
        self.titleLB_2 = QLabel(self.frame)
        self.titleLB_2.setObjectName(u"titleLB_2")
        self.titleLB_2.setGeometry(QRect(200, 150, 221, 41))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.titleLB_2.setFont(font1)
        self.titleLB_2.setStyleSheet(u"color: rgb(0, 0, 0, 0);")
        self.errorLB = QLabel(self.frame)
        self.errorLB.setObjectName(u"errorLB")
        self.errorLB.setGeometry(QRect(120, 400, 311, 20))
        self.errorLB.setStyleSheet(u"color: rgb(229, 9, 20);")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QRect(550, 0, 400, 650))
        self.frame_2.setMinimumSize(QSize(400, 650))
        self.frame_2.setMaximumSize(QSize(400, 650))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.titleLB = QLabel(self.frame_2)
        self.titleLB.setObjectName(u"titleLB")
        self.titleLB.setGeometry(QRect(100, 190, 221, 41))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.titleLB.setFont(font2)
        self.titleLB.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textLB = QLabel(self.frame_2)
        self.textLB.setObjectName(u"textLB")
        self.textLB.setGeometry(QRect(80, 260, 271, 41))
        font3 = QFont()
        font3.setFamilies([u"Heiti SC"])
        font3.setKerning(True)
        self.textLB.setFont(font3)
        self.textLB.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textLB.setLineWidth(1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 300, 351, 31))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setLineWidth(1)
        self.signupBT = QPushButton(self.frame_2)
        self.signupBT.setObjectName(u"signupBT")
        self.signupBT.setGeometry(QRect(120, 370, 161, 41))
        self.signupBT.setFont(font)
        self.signupBT.setStyleSheet(u"background-color: rgb(131, 16, 16);\n"
"border-radius: 15px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.usernameLED.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.loginBT.setText(QCoreApplication.translate("Form", u"Login", None))
        self.passwordLED.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.titleLB_2.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.errorLB.setText("")
        self.titleLB.setText(QCoreApplication.translate("Form", u"New Here?", None))
        self.textLB.setText(QCoreApplication.translate("Form", u"Sign up and discover a great experience", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"on movie journaling with LibMov, your own movie library!", None))
        self.signupBT.setText(QCoreApplication.translate("Form", u"Sign up", None))
    # retranslateUi

