import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from LoginC import LoginC
from SignupC import SignupC
from Stack import StackP

import Main
import Account

class PageSwitch(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(0, 0, 950, 650)

        self.user = None

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login = LoginC()
        self.signup = SignupC()
        self.stackp = StackP(self.user)

        self.setFixedSize(950, 650)

        self.stack.addWidget(self.login)
        self.stack.addWidget(self.signup)
        self.stack.addWidget(self.stackp)

        self.stack.setCurrentWidget(self.login)

        self.login.ui.signupBT.clicked.connect(self.changeToSignup)

        self.signup.ui.backBT.clicked.connect(self.changeToLogin)

        self.login.ui.loginBT.clicked.connect(self.verifyChange)

        self.stackp.hp.ui.logoutBT.clicked.connect(self.CloseChange)
        self.stackp.rv.ui.logoutBT.clicked.connect(self.CloseChange)
        self.stackp.w.ui.logoutBT.clicked.connect(self.CloseChange)
        self.stackp.pf.ui.logoutBT.clicked.connect(self.CloseChange)

    def verifyChange(self):
        self.user = self.login.login_button_verify()
        print(self.user)

        if (self.user != None):
            print("is not none")
            self.stack.setCurrentWidget(self.stackp)

            self.stackp.load(self.user)
    
    def CloseChange(self):
        Main.closeConnection()
        self.stack.setCurrentWidget(self.login)

    def changeToStackP(self):
         self.stack.setCurrentWidget(self.stackp)
        
    def changeToLogin(self):
        self.stack.setCurrentWidget(self.login)

    def changeToSignup(self):
        self.stack.setCurrentWidget(self.signup)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PageSwitch()
    w.show()
    sys.exit(app.exec_())
    
    




    
        