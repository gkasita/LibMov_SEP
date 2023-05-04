import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from HomePageUi import Ui_Form

class HomePageC(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomePageC()
    w.show()
    sys.exit(app.exec_())