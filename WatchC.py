import ZODB, ZODB.FileStorage
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from WatchPageUi import Ui_Form

import Main

root = Main.connection.root()

accounts = root['accounts']


class WatchC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user
    
    def load(self):
        pass

    def addWatched(self):
        pass

    def addWatching(self):
        pass

    def addWillWatch(self):
        pass

    def delWatched(self):
        pass

    def delWatching(self):
        pass

    def delWillWatch(self):
        pass


