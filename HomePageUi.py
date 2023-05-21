# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomePageUi.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
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
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 0, 850, 650))
        self.widget.setMinimumSize(QSize(850, 650))
        self.widget.setMaximumSize(QSize(850, 650))
        self.verticalLayout = QVBoxLayout(self.widget)
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
#endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(850, 80))
        self.widget_2.setMaximumSize(QSize(850, 80))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(500, 20, 231, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(740, 20, 100, 32))
        self.pushButton.setStyleSheet(u"background-color: rgb(131, 16, 16);")

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(850, 150))
        self.widget_3.setMaximumSize(QSize(850, 150))
        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 10, 125, 125))
        self.pushButton_2.setMinimumSize(QSize(125, 125))
        self.pushButton_2.setMaximumSize(QSize(125, 125))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(131, 16, 16);\n"
"border-radius: 15px")
        self.pf_label = QLabel(self.widget_3)
        self.pf_label.setObjectName(u"pf_label")
        self.pf_label.setGeometry(QRect(290, 20, 341, 111))

        self.verticalLayout.addWidget(self.widget_3)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(850, 400))
        self.scrollArea.setMaximumSize(QSize(850, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 874, 398))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(850, 100))
        self.widget_4.setMaximumSize(QSize(850, 100))
        self.widget_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 40, 271, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.widget_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


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
        self.pushButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.pf_label.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Review from this user", None))
    # retranslateUi

