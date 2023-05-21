# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReviewPageUi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

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
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(100, 0, 850, 650))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(850, 650))
        self.scrollArea.setMaximumSize(QSize(850, 650))
        self.scrollArea.setStyleSheet(u"background-color: rgb(86, 77, 77);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 862, 648))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
#endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 10, 20, -1)
        self.scrollArea_7 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMinimumSize(QSize(822, 140))
        self.scrollArea_7.setMaximumSize(QSize(822, 140))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 820, 140))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 140))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
#ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 0, 0)
        self.searchLED = QLineEdit(self.frame_2)
        self.searchLED.setObjectName(u"searchLED")
        self.searchLED.setMinimumSize(QSize(0, 30))
        self.searchLED.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.searchLED)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(350, 30))
        self.widget.setMaximumSize(QSize(350, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(170, 25))
        self.addButton.setMaximumSize(QSize(150, 25))
        self.addButton.setStyleSheet(u"background-color: rgb(131, 16, 16);")

        self.horizontalLayout_3.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.widget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(170, 25))
        self.deleteButton.setMaximumSize(QSize(150, 25))
        self.deleteButton.setStyleSheet(u"background-color: rgb(131, 16, 16);")

        self.horizontalLayout_3.addWidget(self.deleteButton)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(350, 30))
        self.widget_3.setMaximumSize(QSize(350, 25))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.editButton = QPushButton(self.widget_3)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMinimumSize(QSize(170, 25))
        self.editButton.setMaximumSize(QSize(150, 25))
        self.editButton.setStyleSheet(u"background-color: rgb(131, 16, 16);")

        self.horizontalLayout_4.addWidget(self.editButton)

        self.saveButton = QPushButton(self.widget_3)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(170, 25))
        self.saveButton.setMaximumSize(QSize(150, 25))
        self.saveButton.setStyleSheet(u"background-color: rgb(131, 16, 16);")

        self.horizontalLayout_4.addWidget(self.saveButton)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 140))
        self.frame_3.setMaximumSize(QSize(16777215, 140))
        self.frame_3.setSizeIncrement(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.ratingSPB = QSpinBox(self.frame_3)
        self.ratingSPB.setObjectName(u"ratingSPB")
        self.ratingSPB.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.ratingSPB)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.textArea = QPlainTextEdit(self.scrollAreaWidgetContents_7)
        self.textArea.setObjectName(u"textArea")
        self.textArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.textArea)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout.addWidget(self.scrollArea_7)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(800, 220))
        self.widget_2.setMaximumSize(QSize(800, 220))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px")
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 40, 115, 170))
        self.pushButton_3.setMinimumSize(QSize(115, 170))
        self.pushButton_3.setMaximumSize(QSize(115, 170))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.TitleLB = QLabel(self.widget_2)
        self.TitleLB.setObjectName(u"TitleLB")
        self.TitleLB.setGeometry(QRect(40, 20, 241, 16))
        self.reviewArea = QPlainTextEdit(self.widget_2)
        self.reviewArea.setObjectName(u"reviewArea")
        self.reviewArea.setGeometry(QRect(360, 40, 421, 161))
        self.reviewArea.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"padding: 8px;")
        self.movieLB = QLabel(self.widget_2)
        self.movieLB.setObjectName(u"movieLB")
        self.movieLB.setGeometry(QRect(160, 50, 181, 111))
        self.starratingLED = QLineEdit(self.widget_2)
        self.starratingLED.setObjectName(u"starratingLED")
        self.starratingLED.setGeometry(QRect(240, 170, 113, 21))
        self.starratingLED.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"padding: 8px;")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 170, 71, 16))

        self.verticalLayout.addWidget(self.widget_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

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
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Star Rating", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.TitleLB.setText(QCoreApplication.translate("Form", u"Title", None))
        self.movieLB.setText(QCoreApplication.translate("Form", u"Movie Details", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Star Rating:", None))
    # retranslateUi

