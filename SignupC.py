import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from SignupPageUi import Ui_Form

import Main
import Account

root = Main.connection.root()

accounts = root['accounts']

class SignupC(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.signupBT.clicked.connect(self.signup_button_verify)

    def signup_button_verify(self):
        username = self.ui.usernameLED.text()
        password = self.ui.passwordLED.text()
        confirmedpassword = self.ui.cfpasswordLED.text()


        if (self.signup(username, password, confirmedpassword)):
            self.ui.errorLB.setText("sign up successfully")
        else:
            self.ui.errorLB.setText("username already taken or password unmatch")
    
    def signup(self, username, password, confirmed_password):
        if (password == confirmed_password) and (not Main.isUsernameExist(username)):
            accounts[username] = Account.User(username, password)
            print("sign up successfully")
            print(accounts[username].name)
            print(accounts[username].password)
            Main.closeConnection()
            return True
        else:
            #password not match with confirmed password
            print("wrong")
            return False
