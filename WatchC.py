import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from WatchPageUi import Ui_Form

class WatchC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user

    def load(self, user):
        self.user = user
    
    def whichType(self):
        total = 0
        watched = False
        watching = False
        will_watch = False

        if (self.ui.watchedCB.isChecked()):
            watched = True
            total += 1
        if (self.ui.watchingCB.isChecked()):
            watching = True
            total += 1
        if (self.ui.willwatchCB.isChecked()):
            will_watch = True
            total += 1
        
        if (total != 1):
            return False
        elif (watched):
            return "watched"
        elif (watching):
            return "watching"
        elif (will_watch):
            return "will watch"
    
    def addMovie(self, title):
        pass


        
    def removeMovie(self, movie, type):
        pass

    def clear(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WatchC()
    w.show()
    sys.exit(app.exec_())
