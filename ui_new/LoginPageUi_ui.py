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
        self.widget.setGeometry(QRect(0, 0, 951, 650))
        self.widget.setStyleSheet(u"background-color: rgb(243, 240, 209);")
        self.titleLB_2 = QLabel(self.widget)
        self.titleLB_2.setObjectName(u"titleLB_2")
        self.titleLB_2.setGeometry(QRect(275, -10, 400, 400))
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
        self.layoutWidget.setGeometry(QRect(390, 520, 162, 73))
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

        self.signupButton = QPushButton(self.layoutWidget)
        self.signupButton.setObjectName(u"signupButton")
        self.signupButton.setMinimumSize(QSize(75, 25))
        font2 = QFont()
        font2.setFamilies([u"Century Schoolbook"])
        font2.setPointSize(10)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.signupButton.setFont(font2)
        self.signupButton.setCheckable(True)
        self.signupButton.setAutoExclusive(True)
        self.signupButton.setFlat(True)

        self.verticalLayout_3.addWidget(self.signupButton)

        self.layoutWidget_2 = QWidget(self.widget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(320, 390, 304, 118))
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLB_2.setText("")
        self.loginButton.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.signupButton.setText(QCoreApplication.translate("Form", u"No Account?", None))
        self.usernameLED.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLED.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.errorLabel.setText("")
    # retranslateUi

