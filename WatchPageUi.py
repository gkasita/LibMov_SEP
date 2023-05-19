# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WatchPageUi.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

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
        self.scrollArea.setGeometry(QRect(100, 0, 850, 950))
        self.scrollArea.setMinimumSize(QSize(850, 950))
        self.scrollArea.setMaximumSize(QSize(850, 950))
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setStyleSheet(u"background-color: rgb(86, 77, 77);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 848, 1300))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1300))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 1300))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 120))
        self.frame.setMaximumSize(QSize(16777215, 120))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.frame)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 820, 126))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.searchLED = QLineEdit(self.frame_2)
        self.searchLED.setObjectName(u"searchLED")
        self.searchLED.setMinimumSize(QSize(0, 30))
        self.searchLED.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.searchLED)

        self.addButton = QPushButton(self.frame_2)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setStyleSheet(u"background-color: rgb(131, 16, 16);")

        self.verticalLayout_2.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.frame_2)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setStyleSheet(u"background-color: rgb(131, 16, 16);")

        self.verticalLayout_2.addWidget(self.deleteButton)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setSizeIncrement(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.watchedCB = QCheckBox(self.frame_3)
        self.watchedCB.setObjectName(u"watchedCB")

        self.verticalLayout_3.addWidget(self.watchedCB)

        self.watchingCB = QCheckBox(self.frame_3)
        self.watchingCB.setObjectName(u"watchingCB")

        self.verticalLayout_3.addWidget(self.watchingCB)

        self.willwatchCB = QCheckBox(self.frame_3)
        self.willwatchCB.setObjectName(u"willwatchCB")

        self.verticalLayout_3.addWidget(self.willwatchCB)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.textArea = QPlainTextEdit(self.scrollAreaWidgetContents_7)
        self.textArea.setObjectName(u"textArea")
        self.textArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.textArea)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.horizontalLayout.addWidget(self.scrollArea_7)


        self.verticalLayout.addWidget(self.frame)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 200))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(255,  255, 255);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 822, 198))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(115, 170))
        self.pushButton.setMaximumSize(QSize(115, 170))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.scrollArea_3 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 200))
        self.scrollArea_3.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(255,  255, 255);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 822, 198))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(115, 170))
        self.pushButton_2.setMaximumSize(QSize(115, 170))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_3)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_3)

        self.scrollArea_4 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(0, 200))
        self.scrollArea_4.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_4.setStyleSheet(u"background-color: rgb(255,  255, 255);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 822, 198))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(115, 170))
        self.pushButton_3.setMaximumSize(QSize(115, 170))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_5)

        self.scrollArea_6 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 200))
        self.scrollArea_6.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_6.setStyleSheet(u"background-color: rgb(255,  255, 255);")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 822, 198))
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout.addWidget(self.scrollArea_6)

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
        self.watchedCB.setText(QCoreApplication.translate("Form", u"watched", None))
        self.watchingCB.setText(QCoreApplication.translate("Form", u"watching", None))
        self.willwatchCB.setText(QCoreApplication.translate("Form", u"will watch", None))
        self.label.setText(QCoreApplication.translate("Form", u"Watched", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Watching", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Will Watch", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"LibMov", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Others", None))
    # retranslateUi

