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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 650, 650))
        self.widget.setStyleSheet(u"background-color: rgb(243, 240, 209);")
        self.titleLB_2 = QLabel(self.widget)
        self.titleLB_2.setObjectName(u"titleLB_2")
        self.titleLB_2.setGeometry(QRect(125, -10, 400, 400))
        self.titleLB_2.setMinimumSize(QSize(400, 400))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(40)
        font.setBold(True)
        self.titleLB_2.setFont(font)
        self.titleLB_2.setStyleSheet(u"color: rgb(0, 0, 0, 0);")
        self.titleLB_2.setFrameShape(QFrame.NoFrame)
        self.titleLB_2.setFrameShadow(QFrame.Plain)
        self.titleLB_2.setLineWidth(0)
        self.titleLB_2.setPixmap(QPixmap(u":/Icons/Icons/LIBMOV.png"))
        self.titleLB_2.setScaledContents(True)
        self.titleLB_2.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(240, 530, 162, 73))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.loginButton = QPushButton(self.layoutWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(160, 40))
        font1 = QFont()
        font1.setFamilies([u"Century Schoolbook"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.loginButton.setFont(font1)
        self.loginButton.setStyleSheet(u"background-color: rgb(162, 14, 14);\n"
"color: rgb(243, 240, 209);\n"
"border-radius: 15px;")
        self.loginButton.setCheckable(True)
        self.loginButton.setAutoExclusive(True)
        self.loginButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.loginButton)

        self.noAccButton = QPushButton(self.layoutWidget)
        self.noAccButton.setObjectName(u"noAccButton")
        self.noAccButton.setMinimumSize(QSize(75, 25))
        font2 = QFont()
        font2.setFamilies([u"Century Schoolbook"])
        font2.setPointSize(10)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.noAccButton.setFont(font2)
        self.noAccButton.setCheckable(True)
        self.noAccButton.setAutoExclusive(True)
        self.noAccButton.setFlat(True)

        self.verticalLayout_3.addWidget(self.noAccButton)

        self.layoutWidget_2 = QWidget(self.widget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(170, 400, 304, 118))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLED = QLineEdit(self.layoutWidget_2)
        self.usernameLED.setObjectName(u"usernameLED")
        self.usernameLED.setMinimumSize(QSize(300, 40))
        font3 = QFont()
        font3.setFamilies([u"Century Schoolbook"])
        font3.setPointSize(15)
        self.usernameLED.setFont(font3)
        self.usernameLED.setAutoFillBackground(False)
        self.usernameLED.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"border: 2px solid rgb(243, 240, 209);\n"
"border-bottom-color: rgb(162, 14, 14);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.usernameLED.setFrame(True)
        self.usernameLED.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.usernameLED)

        self.passwordLED = QLineEdit(self.layoutWidget_2)
        self.passwordLED.setObjectName(u"passwordLED")
        self.passwordLED.setMinimumSize(QSize(300, 40))
        self.passwordLED.setFont(font3)
        self.passwordLED.setAutoFillBackground(False)
        self.passwordLED.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"border: 2px solid rgb(243, 240, 209);\n"
"border-bottom-color: rgb(162, 14, 14);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.passwordLED.setFrame(True)
        self.passwordLED.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.passwordLED)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.errorLabel = QLabel(self.layoutWidget_2)
        self.errorLabel.setObjectName(u"errorLabel")
        font4 = QFont()
        font4.setFamilies([u"Century Schoolbook"])
        font4.setPointSize(10)
        self.errorLabel.setFont(font4)
        self.errorLabel.setStyleSheet(u"color: rgb(229, 9, 20);")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.errorLabel)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(650, 0, 300, 650))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 9, 44);\n"
"")
        self.layoutWidget_3 = QWidget(self.widget_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 140, 302, 353))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setSpacing(50)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, -1, 2, -1)
        self.titleLB = QLabel(self.layoutWidget_3)
        self.titleLB.setObjectName(u"titleLB")
        font5 = QFont()
        font5.setFamilies([u"Century Schoolbook"])
        font5.setPointSize(38)
        font5.setBold(True)
        self.titleLB.setFont(font5)
        self.titleLB.setStyleSheet(u"color: rgb(243, 240, 209);")
        self.titleLB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.titleLB)

        self.textLB = QLabel(self.layoutWidget_3)
        self.textLB.setObjectName(u"textLB")
        font6 = QFont()
        font6.setFamilies([u"Century Schoolbook"])
        font6.setKerning(True)
        self.textLB.setFont(font6)
        self.textLB.setStyleSheet(u"color: rgb(243, 240, 209);")
        self.textLB.setLineWidth(1)
        self.textLB.setTextFormat(Qt.RichText)
        self.textLB.setScaledContents(False)
        self.textLB.setAlignment(Qt.AlignCenter)
        self.textLB.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.textLB)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.signupButton = QPushButton(self.layoutWidget_3)
        self.signupButton.setObjectName(u"signupButton")
        self.signupButton.setMinimumSize(QSize(160, 40))
        self.signupButton.setFont(font1)
        self.signupButton.setStyleSheet(u"background-color: rgb(162, 14, 14);\n"
"color: rgb(243, 240, 209);\n"
"border-radius: 15px;")
        self.signupButton.setCheckable(True)
        self.signupButton.setAutoExclusive(True)
        self.signupButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.signupButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLB_2.setText("")
        self.loginButton.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.noAccButton.setText(QCoreApplication.translate("Form", u"No Account?", None))
        self.usernameLED.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLED.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.errorLabel.setText("")
        self.titleLB.setText(QCoreApplication.translate("Form", u"New Here?", None))
        self.textLB.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">Sign Up to discover Movie Journaling </span></p><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">with</span><span style=\" font-size:14pt; color:#f3f0d1;\"> LibMov</span><span style=\" font-size:12pt; color:#f3f0d1;\">, </span></p><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">your very own digital </span></p><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">movie journaling library.</span></p></body></html>", None))
        self.signupButton.setText(QCoreApplication.translate("Form", u"SIGN UP", None))
    # retranslateUi

