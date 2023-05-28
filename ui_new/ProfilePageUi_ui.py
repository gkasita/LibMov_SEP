# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfilePageUi.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        Form.setMinimumSize(QSize(950, 650))
        Form.setMaximumSize(QSize(950, 650))
        Form.setSizeIncrement(QSize(300, 200))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.button = QPushButton(Form)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(770, 160, 171, 24))
        font = QFont()
        font.setFamilies([u"Century Schoolbook"])
        font.setPointSize(12)
        self.button.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/settings-3-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QSize(24, 24))
        self.menu = QFrame(Form)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 100, 650))
        self.menu.setMinimumSize(QSize(100, 650))
        self.menu.setMaximumSize(QSize(100, 650))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.menu.setFont(font1)
        self.menu.setStyleSheet(u"background-color: rgb(0, 9, 44);")
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
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/LIBMOV.png", QSize(), QIcon.Normal, QIcon.Off)
        self.libmovBT.setIcon(icon1)
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
        font3 = QFont()
        font3.setFamilies([u"Century Schoolbook"])
        font3.setPointSize(16)
        self.profileBT.setFont(font3)
        self.profileBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.profileBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.profileBT)

        self.reviewBT = QPushButton(self.layoutWidget)
        self.reviewBT.setObjectName(u"reviewBT")
        self.reviewBT.setMinimumSize(QSize(100, 50))
        self.reviewBT.setMaximumSize(QSize(100, 50))
        self.reviewBT.setFont(font3)
        self.reviewBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.reviewBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.reviewBT)

        self.watchBT = QPushButton(self.layoutWidget)
        self.watchBT.setObjectName(u"watchBT")
        self.watchBT.setMinimumSize(QSize(100, 50))
        self.watchBT.setMaximumSize(QSize(100, 50))
        self.watchBT.setFont(font3)
        self.watchBT.setStyleSheet(u"color:rgb(243, 240, 209);")
        self.watchBT.setFlat(True)

        self.verticalLayout_4.addWidget(self.watchBT)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.logoutBT = QPushButton(self.layoutWidget)
        self.logoutBT.setObjectName(u"logoutBT")
        self.logoutBT.setMinimumSize(QSize(100, 50))
        self.logoutBT.setMaximumSize(QSize(100, 50))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(15)
        font4.setBold(False)
        self.logoutBT.setFont(font4)
        self.logoutBT.setStyleSheet(u"background-color: rgb(243, 240, 209);\n"
"border-radius: 25px;\n"
"border-color: rgb(0, 9, 44);")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/logout-box-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBT.setIcon(icon2)
        self.logoutBT.setIconSize(QSize(30, 30))
        self.logoutBT.setFlat(False)

        self.verticalLayout_4.addWidget(self.logoutBT)

        self.layoutWidget.raise_()
        self.libmovBT.raise_()
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 0, 850, 150))
        self.label_8.setPixmap(QPixmap(u":/Icons/Icons/Profile Title Card.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 80, 432, 242))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(75, 75))
        self.label_9.setPixmap(QPixmap(u":/Icons/Icons/user-star-line.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_9)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(250, 75))
        font5 = QFont()
        font5.setFamilies([u"Century Schoolbook"])
        font5.setPointSize(25)
        self.label.setFont(font5)

        self.horizontalLayout.addWidget(self.label)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(270, 340, 531, 78))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setSpacing(75)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"Century Schoolbook"])
        font6.setPointSize(15)
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button.setText(QCoreApplication.translate("Form", u"Change Password", None))
        self.libmovBT.setText("")
        self.profileBT.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.reviewBT.setText(QCoreApplication.translate("Form", u"Review", None))
        self.watchBT.setText(QCoreApplication.translate("Form", u"MyLists", None))
        self.logoutBT.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"User Profile", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Watched", None))
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Watching", None))
        self.label_3.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Will Watch", None))
        self.label_4.setText("")
    # retranslateUi

