import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from ReviewPageUi import Ui_Form

class ReviewC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user
    
    def load(self, user):
        self.user = user



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ReviewC()
    w.show()
    sys.exit(app.exec_())
