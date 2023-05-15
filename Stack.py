import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from HomePageC import HomePageC
from ReviewC import ReviewC
from WatchC import WatchC
from ProfileC import ProfileC


#when login successfully, the system return and call this object with username as parameter

#each of pages self.hp, self.rv, self.w, self.wc, and self.ww have to have the method to download all info
#each C class will take username as parameter to retrieve data from database
class StackP(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.setGeometry(0, 0, 950, 650)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.user = user

        self.hp = HomePageC()
        self.rv = ReviewC(user)
        self.w = WatchC(user)
        self.pf = ProfileC(user)

        self.setFixedSize(950, 650)

        self.stack.addWidget(self.hp)
        self.stack.addWidget(self.rv)
        self.stack.addWidget(self.w)
        self.stack.addWidget(self.pf)

        self.hp.ui.libmovBT.clicked.connect(self.change_to_hp)
        self.hp.ui.reviewBT.clicked.connect(self.change_to_rv)
        self.hp.ui.watchBT.clicked.connect(self.change_to_w)
        self.hp.ui.profileBT.clicked.connect(self.change_to_pf)
    
        self.rv.ui.libmovBT.clicked.connect(self.change_to_hp)
        self.rv.ui.reviewBT.clicked.connect(self.change_to_rv)
        self.rv.ui.watchBT.clicked.connect(self.change_to_w)
        self.rv.ui.profileBT.clicked.connect(self.change_to_pf)

        self.w.ui.libmovBT.clicked.connect(self.change_to_hp)
        self.w.ui.reviewBT.clicked.connect(self.change_to_rv)
        self.w.ui.watchBT.clicked.connect(self.change_to_w)
        self.w.ui.profileBT.clicked.connect(self.change_to_pf)

        self.pf.ui.libmovBT.clicked.connect(self.change_to_hp)
        self.pf.ui.reviewBT.clicked.connect(self.change_to_rv)
        self.pf.ui.watchBT.clicked.connect(self.change_to_w)
        self.pf.ui.profileBT.clicked.connect(self.change_to_pf)

    def change_to_pf(self):
        self.stack.setCurrentWidget(self.pf)
        
    def change_to_hp(self):
        self.stack.setCurrentWidget(self.hp)

    def change_to_rv(self):
        self.stack.setCurrentWidget(self.rv)

    def change_to_w(self):
        self.stack.setCurrentWidget(self.w)
    
    def load(self, user):
        self.rv.user =  user
        self.w.user = user
        self.pf.user = user
        
        self.pf.load()
        self.w.load()


    
    




    
        