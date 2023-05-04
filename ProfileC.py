import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ProfilePageUi import Ui_Form

import Account

class ProfileC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = Account.User

    
    def load(self):
        self.ui.label.setText("Hi, " + self.user.name + ", password " + self.user.password)
