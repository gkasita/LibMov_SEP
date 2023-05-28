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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(100, 0, 850, 650))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(850, 500))
        self.scrollArea.setMaximumSize(QSize(850, 650))
        self.scrollArea.setStyleSheet(u"background-color: rgb(242, 232, 198);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 855, 631))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 5, 5)
        self.scrollArea_7 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMinimumSize(QSize(850, 150))
        self.scrollArea_7.setMaximumSize(QSize(850, 150))
        self.scrollArea_7.setStyleSheet(u"background-color: rgb(0, 9, 44);")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 848, 148))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 140))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.searchLED = QLineEdit(self.frame_2)
        self.searchLED.setObjectName(u"searchLED")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchLED.sizePolicy().hasHeightForWidth())
        self.searchLED.setSizePolicy(sizePolicy1)
        self.searchLED.setMinimumSize(QSize(350, 40))
        font = QFont()
        font.setFamilies([u"Century Schoolbook"])
        font.setPointSize(15)
        self.searchLED.setFont(font)
        self.searchLED.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.searchLED)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(350, 30))
        self.widget.setMaximumSize(QSize(350, 25))
        self.layoutWidget_4 = QWidget(self.widget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(1, 2, 348, 27))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.layoutWidget_4)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(170, 25))
        self.addButton.setMaximumSize(QSize(150, 25))
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

        self.horizontalLayout_5.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.layoutWidget_4)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(170, 25))
        self.deleteButton.setMaximumSize(QSize(150, 25))
        self.deleteButton.setFont(font1)
        self.deleteButton.setStyleSheet(u"background-color:  rgb(242, 232, 198);;\n"
"color: rgb(0, 9, 44);")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/delete-bin-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.deleteButton)


        self.verticalLayout_7.addWidget(self.widget)

        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(350, 30))
        self.widget_3.setMaximumSize(QSize(350, 25))
        self.layoutWidget_5 = QWidget(self.widget_3)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(1, 2, 348, 27))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.editButton = QPushButton(self.layoutWidget_5)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMinimumSize(QSize(170, 25))
        self.editButton.setMaximumSize(QSize(150, 25))
        self.editButton.setFont(font1)
        self.editButton.setStyleSheet(u"background-color:  rgb(242, 232, 198);;\n"
"color: rgb(0, 9, 44);")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/edit-2-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.editButton)

        self.saveButton = QPushButton(self.layoutWidget_5)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(170, 25))
        self.saveButton.setMaximumSize(QSize(150, 25))
        self.saveButton.setFont(font1)
        self.saveButton.setStyleSheet(u"background-color:  rgb(242, 232, 198);;\n"
"color: rgb(0, 9, 44);")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/save-3-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.saveButton)


        self.verticalLayout_7.addWidget(self.widget_3)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 140))
        self.frame_3.setMaximumSize(QSize(16777215, 140))
        self.frame_3.setSizeIncrement(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(85, 85))
        self.label.setMaximumSize(QSize(85, 85))
        self.label.setStyleSheet(u"background-color: rgb(243, 240, 209);")
        self.label.setPixmap(QPixmap(u":/Icons/Icons/star-line.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.ratingSPB = QSpinBox(self.frame_3)
        self.ratingSPB.setObjectName(u"ratingSPB")
        self.ratingSPB.setMinimumSize(QSize(0, 30))
        self.ratingSPB.setFont(font1)
        self.ratingSPB.setStyleSheet(u"background-color:rgb(243, 240, 209)")
        self.ratingSPB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ratingSPB)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.textArea = QPlainTextEdit(self.scrollAreaWidgetContents_7)
        self.textArea.setObjectName(u"textArea")
        self.textArea.setMinimumSize(QSize(0, 140))
        self.textArea.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamilies([u"Century Schoolbook"])
        font2.setPointSize(10)
        self.textArea.setFont(font2)
        self.textArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.textArea)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout.addWidget(self.scrollArea_7)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(800, 100))
        self.widget_2.setMaximumSize(QSize(850, 100))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(850, 100))
        self.label_3.setMaximumSize(QSize(16777215, 100))
        self.label_3.setPixmap(QPixmap(u":/Icons/Icons/Review-Journal.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.widget_2)

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
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/LIBMOV.png", QSize(), QIcon.Normal, QIcon.Off)
        self.libmovBT.setIcon(icon4)
        self.libmovBT.setIconSize(QSize(100, 100))
        self.libmovBT.setFlat(False)
        self.layoutWidget = QWidget(self.menu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 102, 551))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.profileBT = QPushButton(self.layoutWidget)
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

        self.reviewBT = QPushButton(self.layoutWidget)
        self.reviewBT.setObjectName(u"reviewBT")
        self.reviewBT.setMinimumSize(QSize(100, 50))
        self.reviewBT.setMaximumSize(QSize(100, 50))
        self.reviewBT.setFont(font5)
        self.reviewBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.reviewBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.reviewBT)

        self.watchBT = QPushButton(self.layoutWidget)
        self.watchBT.setObjectName(u"watchBT")
        self.watchBT.setMinimumSize(QSize(100, 50))
        self.watchBT.setMaximumSize(QSize(100, 50))
        self.watchBT.setFont(font5)
        self.watchBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.watchBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.watchBT)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.logoutBT = QPushButton(self.layoutWidget)
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
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/logout-box-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBT.setIcon(icon5)
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
        self.label_2.setText("")
        self.addButton.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"EDIT", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.label.setText("")
        self.label_3.setText("")
        self.libmovBT.setText("")
        self.profileBT.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.reviewBT.setText(QCoreApplication.translate("Form", u"Review", None))
        self.watchBT.setText(QCoreApplication.translate("Form", u"MyLists", None))
        self.logoutBT.setText("")
    # retranslateUi

