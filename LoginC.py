import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from LoginPageUi import Ui_Form
import Main

root = Main.connection.root()

accounts = root['accounts']


class LoginC(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    
    def login_button_verify(self):
        username = self.ui.usernameLED.text()
        password = self.ui.passwordLED.text()


        tmp = self.verifyUsername(username, password)
        if (tmp == True):
            self.ui.errorLB.setText("log in successfully")
            return accounts[username]
        else:
            self.ui.errorLB.setText("invalid username or password")
            return None
        
    def verifyUsername(self, username, password):
        tmp = False
        keys = accounts.keys()
        for key in keys:
            #username already exist
            if username == key:
                tmp = True
        if (tmp == True):
            if (accounts[username].password == password):
                return True
        else:
            return False    
    


     

