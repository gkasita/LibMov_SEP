import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from LoginPageUi import Ui_Form
import LSCode

#Ui - usernameLED, passwordLED, loginButton, signupButton
class LoginC(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoginC()
    w.show()
    sys.exit(app.exec_())




    