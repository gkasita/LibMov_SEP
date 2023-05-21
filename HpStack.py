import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

import Account
import Connection

import HomePageC
import ProfileC
import ReviewC
import WatchC

class HpStack(QMainWindow):
    def __init__(self, user):
        self.user = user
        QMainWindow.__init__(self)
        self.setGeometry(0, 0, 950, 650)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.hp = HomePageC.HomePageC()
        self.rv = ReviewC.ReviewC(user)
        self.w = WatchC.WatchC(user)
        self.pf = ProfileC.ProfileC(user)

        self.setFixedSize(950, 650)

        self.stack.addWidget(self.hp)
        self.stack.addWidget(self.rv)
        self.stack.addWidget(self.w)
        self.stack.addWidget(self.pf)

        self.stack.setCurrentWidget(self.pf)

        self.hp.ui.libmovBT.clicked.connect(self.changeToHp)
        self.hp.ui.reviewBT.clicked.connect(self.changeToRv)
        self.hp.ui.watchBT.clicked.connect(self.changeToW)
        self.hp.ui.profileBT.clicked.connect(self.changeToPf)
    
        self.rv.ui.libmovBT.clicked.connect(self.changeToHp)
        self.rv.ui.reviewBT.clicked.connect(self.changeToRv)
        self.rv.ui.watchBT.clicked.connect(self.changeToW)
        self.rv.ui.profileBT.clicked.connect(self.changeToPf)

        self.w.ui.libmovBT.clicked.connect(self.changeToHp)
        self.w.ui.reviewBT.clicked.connect(self.changeToRv)
        self.w.ui.watchBT.clicked.connect(self.changeToW)
        self.w.ui.profileBT.clicked.connect(self.changeToPf)

        self.pf.ui.libmovBT.clicked.connect(self.changeToHp)
        self.pf.ui.reviewBT.clicked.connect(self.changeToRv)
        self.pf.ui.watchBT.clicked.connect(self.changeToW)
        self.pf.ui.profileBT.clicked.connect(self.changeToPf)

    
    def load(self, username):
        u1 = Connection.Connection.getUser(username)
        print('HpStack load function')
        self.user = u1

        self.rv.load(u1)
        self.w.load(u1)
        self.pf.load(u1)

    def changeToHp(self):
        self.stack.setCurrentWidget(self.hp)

    def changeToPf(self):
        self.stack.setCurrentWidget(self.pf)
        
    def changeToRv(self):
        self.stack.setCurrentWidget(self.rv)

    def changeToW(self):
        self.stack.setCurrentWidget(self.w)



    
    




    
        