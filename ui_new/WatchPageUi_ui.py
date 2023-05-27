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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
        Form.setStyleSheet(u"background-color: rgb(243, 240, 209);")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 900, 1300))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1300))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 1300))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.scrollArea_7.setStyleSheet(u"background-color: rgb(0, 9, 44);")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 896, 116))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 281, 91))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.searchLED = QLineEdit(self.layoutWidget)
        self.searchLED.setObjectName(u"searchLED")
        self.searchLED.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamilies([u"Century Schoolbook"])
        font.setPointSize(15)
        self.searchLED.setFont(font)
        self.searchLED.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.searchLED)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.addButton = QPushButton(self.layoutWidget)
        self.addButton.setObjectName(u"addButton")
        font1 = QFont()
        font1.setFamilies([u"Century Schoolbook"])
        font1.setPointSize(13)
        self.addButton.setFont(font1)
        self.addButton.setStyleSheet(u"background-color:  rgb(242, 232, 198);;\n"
"color: rgb(0, 9, 44);")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/add-circle-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.layoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setFont(font1)
        self.deleteButton.setStyleSheet(u"background-color:  rgb(242, 232, 198);;\n"
"color: rgb(0, 9, 44);")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/close-circle-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.deleteButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setSizeIncrement(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.watchedCB = QCheckBox(self.frame_3)
        self.watchedCB.setObjectName(u"watchedCB")
        font2 = QFont()
        font2.setFamilies([u"Century Schoolbook"])
        font2.setPointSize(10)
        self.watchedCB.setFont(font2)
        self.watchedCB.setStyleSheet(u"color: rgb(243, 240, 209)")

        self.verticalLayout_3.addWidget(self.watchedCB)

        self.watchingCB = QCheckBox(self.frame_3)
        self.watchingCB.setObjectName(u"watchingCB")
        self.watchingCB.setFont(font2)
        self.watchingCB.setStyleSheet(u"color: rgb(243, 240, 209)")

        self.verticalLayout_3.addWidget(self.watchingCB)

        self.willwatchCB = QCheckBox(self.frame_3)
        self.willwatchCB.setObjectName(u"willwatchCB")
        self.willwatchCB.setFont(font2)
        self.willwatchCB.setStyleSheet(u"color: rgb(243, 240, 209)")

        self.verticalLayout_3.addWidget(self.willwatchCB)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.textArea = QPlainTextEdit(self.scrollAreaWidgetContents_7)
        self.textArea.setObjectName(u"textArea")
        self.textArea.setFont(font2)
        self.textArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.textArea)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.horizontalLayout.addWidget(self.scrollArea_7)


        self.verticalLayout.addWidget(self.frame)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 100))
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setLineWidth(1)
        self.label.setPixmap(QPixmap(u":/Icons/Icons/Watched.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label)

        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 200))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(242, 232, 198);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 898, 198))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(115, 170))
        self.pushButton.setMaximumSize(QSize(115, 170))
        self.pushButton.setStyleSheet(u"background-color: rgb(242, 232, 198);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/skip-back-line_big.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(150, 150))
        self.pushButton.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 100))
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setLineWidth(1)
        self.label_2.setPixmap(QPixmap(u":/Icons/Icons/Watching.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(0)

        self.verticalLayout.addWidget(self.label_2)

        self.scrollArea_3 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 200))
        self.scrollArea_3.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(242, 232, 198);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 898, 198))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(115, 170))
        self.pushButton_2.setMaximumSize(QSize(115, 170))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(242, 232, 198);\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/play-line_big.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(150, 150))
        self.pushButton_2.setAutoRepeatDelay(0)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea_3)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 100))
        self.label_3.setMaximumSize(QSize(16777215, 100))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setPixmap(QPixmap(u":/Icons/Icons/Will Watch.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.scrollArea_4 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(0, 200))
        self.scrollArea_4.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_4.setStyleSheet(u"background-color: rgb(242, 232, 198);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 898, 198))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(115, 170))
        self.pushButton_3.setMaximumSize(QSize(115, 170))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(242, 232, 198);\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/skip-forward-line_big.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(150, 150))
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 100))
        self.label_5.setMaximumSize(QSize(16777215, 150))
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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 898, 198))
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout.addWidget(self.scrollArea_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.menu = QFrame(Form)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 100, 650))
        self.menu.setMinimumSize(QSize(100, 650))
        self.menu.setMaximumSize(QSize(100, 650))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        self.menu.setFont(font3)
        self.menu.setStyleSheet(u"background-color: rgb(0, 9, 44);")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.libmovBT = QPushButton(self.menu)
        self.libmovBT.setObjectName(u"libmovBT")
        self.libmovBT.setGeometry(QRect(0, 0, 100, 100))
        self.libmovBT.setMinimumSize(QSize(100, 100))
        self.libmovBT.setMaximumSize(QSize(100, 100))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(15)
        font4.setBold(True)
        self.libmovBT.setFont(font4)
        self.libmovBT.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"color: rgb(131, 16, 16);")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/LIBMOV.png", QSize(), QIcon.Normal, QIcon.Off)
        self.libmovBT.setIcon(icon5)
        self.libmovBT.setIconSize(QSize(100, 100))
        self.libmovBT.setFlat(False)
        self.layoutWidget1 = QWidget(self.menu)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 100, 102, 551))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.profileBT = QPushButton(self.layoutWidget1)
        self.profileBT.setObjectName(u"profileBT")
        self.profileBT.setMinimumSize(QSize(100, 50))
        self.profileBT.setMaximumSize(QSize(100, 50))
        font5 = QFont()
        font5.setFamilies([u"Century Schoolbook"])
        font5.setPointSize(16)
        self.profileBT.setFont(font5)
        self.profileBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.profileBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.profileBT)

        self.reviewBT = QPushButton(self.layoutWidget1)
        self.reviewBT.setObjectName(u"reviewBT")
        self.reviewBT.setMinimumSize(QSize(100, 50))
        self.reviewBT.setMaximumSize(QSize(100, 50))
        self.reviewBT.setFont(font5)
        self.reviewBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.reviewBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.reviewBT)

        self.watchBT = QPushButton(self.layoutWidget1)
        self.watchBT.setObjectName(u"watchBT")
        self.watchBT.setMinimumSize(QSize(100, 50))
        self.watchBT.setMaximumSize(QSize(100, 50))
        self.watchBT.setFont(font5)
        self.watchBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.watchBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.watchBT)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.logoutBT = QPushButton(self.layoutWidget1)
        self.logoutBT.setObjectName(u"logoutBT")
        self.logoutBT.setMinimumSize(QSize(100, 50))
        self.logoutBT.setMaximumSize(QSize(100, 50))
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(15)
        font6.setBold(False)
        self.logoutBT.setFont(font6)
        self.logoutBT.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"border-radius: 25px;\n"
"border-color: rgb(0, 9, 44);")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/logout-box-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBT.setIcon(icon6)
        self.logoutBT.setIconSize(QSize(30, 30))
        self.logoutBT.setFlat(False)

        self.verticalLayout_4.addWidget(self.logoutBT)

        self.layoutWidget.raise_()
        self.libmovBT.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.searchLED.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Movie...", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.watchedCB.setText(QCoreApplication.translate("Form", u"WATCHED", None))
        self.watchingCB.setText(QCoreApplication.translate("Form", u"WATCHING", None))
        self.willwatchCB.setText(QCoreApplication.translate("Form", u"WILL WATCH", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.label_2.setText("")
        self.pushButton_2.setText("")
        self.label_3.setText("")
        self.pushButton_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Others", None))
        self.libmovBT.setText("")
        self.profileBT.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.reviewBT.setText(QCoreApplication.translate("Form", u"Review", None))
        self.watchBT.setText(QCoreApplication.translate("Form", u"MyLists", None))
        self.logoutBT.setText("")
    # retranslateUi

