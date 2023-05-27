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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
        font = QFont()
        font.setFamilies([u"Century Schoolbook"])
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(243, 240, 209);")
        self.menu = QFrame(Form)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 100, 650))
        self.menu.setMinimumSize(QSize(100, 650))
        self.menu.setMaximumSize(QSize(100, 650))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.menu.setFont(font1)
        self.menu.setStyleSheet(u"background-color: rgb(187, 0, 41)\n"
"")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.libmovBT = QPushButton(self.menu)
        self.libmovBT.setObjectName(u"libmovBT")
        self.libmovBT.setGeometry(QRect(0, 0, 100, 100))
        self.libmovBT.setMinimumSize(QSize(100, 100))
        self.libmovBT.setMaximumSize(QSize(100, 100))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.libmovBT.setFont(font2)
        self.libmovBT.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"color: rgb(131, 16, 16);")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/LIBMOV.png", QSize(), QIcon.Normal, QIcon.Off)
        self.libmovBT.setIcon(icon)
        self.libmovBT.setIconSize(QSize(100, 100))
        self.libmovBT.setFlat(False)
        self.layoutWidget = QWidget(self.menu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 102, 551))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.profileBT = QPushButton(self.layoutWidget)
        self.profileBT.setObjectName(u"profileBT")
        self.profileBT.setMinimumSize(QSize(100, 50))
        self.profileBT.setMaximumSize(QSize(100, 50))
        font3 = QFont()
        font3.setFamilies([u"Century Schoolbook"])
        font3.setPointSize(16)
        self.profileBT.setFont(font3)
        self.profileBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.profileBT.setFlat(True)

        self.verticalLayout_3.addWidget(self.profileBT)

        self.reviewBT = QPushButton(self.layoutWidget)
        self.reviewBT.setObjectName(u"reviewBT")
        self.reviewBT.setMinimumSize(QSize(100, 50))
        self.reviewBT.setMaximumSize(QSize(100, 50))
        self.reviewBT.setFont(font3)
        self.reviewBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.reviewBT.setFlat(True)

        self.verticalLayout_3.addWidget(self.reviewBT)

        self.watchBT = QPushButton(self.layoutWidget)
        self.watchBT.setObjectName(u"watchBT")
        self.watchBT.setMinimumSize(QSize(100, 50))
        self.watchBT.setMaximumSize(QSize(100, 50))
        self.watchBT.setFont(font3)
        self.watchBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.watchBT.setFlat(True)

        self.verticalLayout_3.addWidget(self.watchBT)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logoutBT = QPushButton(self.layoutWidget)
        self.logoutBT.setObjectName(u"logoutBT")
        self.logoutBT.setMinimumSize(QSize(100, 50))
        self.logoutBT.setMaximumSize(QSize(100, 50))
        self.logoutBT.setFont(font2)
        self.logoutBT.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/logout-box-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBT.setIcon(icon1)
        self.logoutBT.setIconSize(QSize(30, 30))
        self.logoutBT.setFlat(True)

        self.verticalLayout_3.addWidget(self.logoutBT)

        self.layoutWidget.raise_()
        self.libmovBT.raise_()
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 0, 850, 650))
        self.widget.setMinimumSize(QSize(850, 650))
        self.widget.setMaximumSize(QSize(850, 650))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(950, 100))
        self.widget_2.setMaximumSize(QSize(850, 100))
        self.widget_2.setStyleSheet(u"background-color:rgb(187, 0, 41)")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(500, 30, 230, 30))
        font4 = QFont()
        font4.setFamilies([u"Century Schoolbook"])
        font4.setPointSize(12)
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"background-color: rgb(243, 240, 209);")
        self.lineEdit.setFrame(False)
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(740, 30, 35, 30))
        self.pushButton.setStyleSheet(u"background-color: rgb(243, 240, 209)")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/search-2-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(24, 24))

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
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 9, 44);\n"
"color: rgb(243, 240, 209);\n"
"border-radius: 15px")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/LIBMOV (H2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(125, 125))
        self.pf_label = QLabel(self.widget_3)
        self.pf_label.setObjectName(u"pf_label")
        self.pf_label.setGeometry(QRect(290, 20, 341, 111))

        self.verticalLayout.addWidget(self.widget_3)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(850, 400))
        self.scrollArea.setMaximumSize(QSize(850, 400))
        self.scrollArea.setStyleSheet(u"background-color: rgb(242, 232, 198);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-19, 0, 850, 400))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(850, 400))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(850, 100))
        self.widget_4.setMaximumSize(QSize(850, 100))
        self.widget_4.setStyleSheet(u"background-color:rgb(0, 9, 44);")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(275, -100, 300, 300))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setPixmap(QPixmap(u":/Icons/Icons/LIBMOV (H2).png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.widget_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.widget.raise_()
        self.menu.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.libmovBT.setText("")
        self.profileBT.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.reviewBT.setText(QCoreApplication.translate("Form", u"Review", None))
        self.watchBT.setText(QCoreApplication.translate("Form", u"MyLists", None))
        self.logoutBT.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"SEARCH...", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pf_label.setText("")
        self.label.setText("")
    # retranslateUi

