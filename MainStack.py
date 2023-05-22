import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *


import LoginC
import SignupC
import HpStack

import LSCode

class MainStack(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(0, 0, 950, 650)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login = LoginC.LoginC()
        self.signup = SignupC.SignupC()
        self.stackp = HpStack.HpStack(None)

        self.stack.addWidget(self.login)
        self.stack.addWidget(self.signup)
        self.stack.addWidget(self.stackp)
        self.stack.setCurrentWidget(self.login)

        self.login.ui.signupButton.clicked.connect(self.changeToSignup)
        self.signup.ui.backButton.clicked.connect(self.changeToLogin)

        self.login.ui.loginButton.clicked.connect(self.changeToProgram)

        self.stackp.hp.ui.logoutBT.clicked.connect(self.changeToLogin_Logout)
        self.stackp.rv.ui.logoutBT.clicked.connect(self.changeToLogin_Logout)
        self.stackp.w.ui.logoutBT.clicked.connect(self.changeToLogin_Logout)
        self.stackp.pf.ui.logoutBT.clicked.connect(self.changeToLogin_Logout)
    
    
    def changeToProgram(self):
        username = self.login.ui.usernameLED.text()
        password = self.login.ui.passwordLED.text()

        if(LSCode.LS.verifyPassword(username, password)):
            self.stack.setCurrentWidget(self.stackp)
            self.stackp.load(username)
        else:
            self.login.ui.errorLabel.setText('invalid username or password')
    
    def changeToSignup(self):
        self.stack.setCurrentWidget(self.signup)
    
    def changeToLogin(self):
        self.stack.setCurrentWidget(self.login)
    
    def changeToLogin_Logout(self):
        self.stackp.w.clear()
        self.stackp.rv.clear()
        self.stackp.hp.clear()
        self.stack.setCurrentWidget(self.login)
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainStack()
    w.show()
    sys.exit(app.exec_())
