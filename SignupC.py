import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from SignupPageUi import Ui_Form
import LSCode

class SignupC(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.signupButton.clicked.connect(self.signup)
    
    def signup(self):
        username = self.ui.usernameLED.text()
        password = self.ui.passwordLED.text()
        confirmed_password = self.ui.confirmedPasswordLED.text()

        if(LSCode.LS.signup(username, password, confirmed_password)):
            self.ui.errorLabel.setText('Sign up Successfully')
            print('sign up successfully')
        else:
            self.ui.errorLabel.setText('Username already taken or unmatch password')
            print('username already taken or unmatch password')




    