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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

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
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 9, 44);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.backButton = QPushButton(self.frame_2)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(120, 540, 160, 40))
        self.backButton.setMinimumSize(QSize(160, 40))
        font = QFont()
        font.setFamilies([u"Century Schoolbook"])
        font.setPointSize(18)
        font.setBold(True)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet(u"background-color: rgb(162, 14, 14);\n"
"color: rgb(243, 240, 209);\n"
"border-radius: 15px;")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/arrow-left-s-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(24, 24))
        self.backButton.setFlat(True)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 180, 401, 285))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleLB_2 = QLabel(self.widget)
        self.titleLB_2.setObjectName(u"titleLB_2")
        font1 = QFont()
        font1.setFamilies([u"Century Schoolbook"])
        font1.setPointSize(38)
        font1.setBold(True)
        self.titleLB_2.setFont(font1)
        self.titleLB_2.setStyleSheet(u"color: rgb(243, 240, 209);")
        self.titleLB_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.titleLB_2)

        self.textLB_2 = QLabel(self.widget)
        self.textLB_2.setObjectName(u"textLB_2")
        font2 = QFont()
        font2.setFamilies([u"Century Schoolbook"])
        font2.setKerning(True)
        self.textLB_2.setFont(font2)
        self.textLB_2.setStyleSheet(u"color: rgb(243, 240, 209);")
        self.textLB_2.setLineWidth(1)
        self.textLB_2.setTextFormat(Qt.RichText)
        self.textLB_2.setScaledContents(False)
        self.textLB_2.setAlignment(Qt.AlignCenter)
        self.textLB_2.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.textLB_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(400, 0, 550, 650))
        self.frame.setMinimumSize(QSize(550, 650))
        self.frame.setMaximumSize(QSize(550, 650))
        self.frame.setStyleSheet(u"background-color: rgb(243, 240, 209);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.signupButton = QPushButton(self.frame)
        self.signupButton.setObjectName(u"signupButton")
        self.signupButton.setGeometry(QRect(195, 540, 160, 40))
        self.signupButton.setFont(font)
        self.signupButton.setStyleSheet(u"background-color: rgb(162, 14, 14);\n"
"color: rgb(243, 240, 209);\n"
"border-radius: 15px;")
        self.signupButton.setFlat(True)
        self.logo_label = QLabel(self.frame)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(125, 20, 300, 300))
        self.logo_label.setMinimumSize(QSize(300, 300))
        font3 = QFont()
        font3.setFamilies([u"Al Nile"])
        font3.setPointSize(40)
        font3.setBold(True)
        self.logo_label.setFont(font3)
        self.logo_label.setPixmap(QPixmap(u":/Icons/Icons/LIBMOV.png"))
        self.logo_label.setScaledContents(True)
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(120, 320, 304, 200))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLED = QLineEdit(self.widget1)
        self.usernameLED.setObjectName(u"usernameLED")
        self.usernameLED.setMinimumSize(QSize(300, 40))
        font4 = QFont()
        font4.setFamilies([u"Century Schoolbook"])
        font4.setPointSize(15)
        self.usernameLED.setFont(font4)
        self.usernameLED.setAutoFillBackground(False)
        self.usernameLED.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"border: 2px solid rgb(243, 240, 209);\n"
"border-bottom-color: rgb(162, 14, 14);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.usernameLED.setFrame(True)

        self.verticalLayout.addWidget(self.usernameLED)

        self.passwordLED = QLineEdit(self.widget1)
        self.passwordLED.setObjectName(u"passwordLED")
        self.passwordLED.setMinimumSize(QSize(300, 40))
        self.passwordLED.setFont(font4)
        self.passwordLED.setAutoFillBackground(False)
        self.passwordLED.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"border: 2px solid rgb(243, 240, 209);\n"
"border-bottom-color: rgb(162, 14, 14);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.passwordLED.setFrame(True)

        self.verticalLayout.addWidget(self.passwordLED)

        self.confirmedPasswordLED = QLineEdit(self.widget1)
        self.confirmedPasswordLED.setObjectName(u"confirmedPasswordLED")
        self.confirmedPasswordLED.setMinimumSize(QSize(300, 40))
        self.confirmedPasswordLED.setFont(font4)
        self.confirmedPasswordLED.setAutoFillBackground(False)
        self.confirmedPasswordLED.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"border: 2px solid rgb(243, 240, 209);\n"
"border-bottom-color: rgb(162, 14, 14);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 8px;")
        self.confirmedPasswordLED.setFrame(True)

        self.verticalLayout.addWidget(self.confirmedPasswordLED)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.errorLabel = QLabel(self.widget1)
        self.errorLabel.setObjectName(u"errorLabel")
        font5 = QFont()
        font5.setFamilies([u"Century Schoolbook"])
        font5.setPointSize(10)
        self.errorLabel.setFont(font5)
        self.errorLabel.setStyleSheet(u"color: rgb(162, 14, 14);")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.errorLabel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"BACK", None))
        self.titleLB_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Welcome to </p><p>LibMov!</p></body></html>", None))
        self.textLB_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">Sign Up to explore and discover </span></p><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">Movie Journaling with</span><span style=\" font-size:14pt; color:#f3f0d1;\"> LibMov</span><span style=\" font-size:12pt; color:#f3f0d1;\">, </span></p><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">your very own digital </span></p><p align=\"center\"><span style=\" font-size:12pt; color:#f3f0d1;\">movie journaling library.</span></p></body></html>", None))
        self.signupButton.setText(QCoreApplication.translate("Form", u"SIGN UP", None))
        self.logo_label.setText("")
        self.usernameLED.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLED.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.confirmedPasswordLED.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.errorLabel.setText("")
    # retranslateUi

