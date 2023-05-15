import ZODB, ZODB.FileStorage
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from WatchPageUi import Ui_Form

import Main
import Account

root = Main.connection.root()

accounts = root['accounts']

class WatchC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user
        self.ui.addBT.clicked.connect(self.addWatched)

        self.ui.delBT.clicked.connect(self.clear)
    
    def load(self):
        for m in self.user.watchedlist.movielist:
            bt = QPushButton(m.title)
            bt.setMinimumSize(100, 150)
            bt.setMaximumSize(100, 150)
            self.ui.horizontalLayout_3.addWidget(bt)


    def addWatched(self):
        text = self.ui.lineEdit.text()
        m = Account.Movie(text)
        self.user.watchedlist.addMovie(m)

        bt = QPushButton(text)
        bt.setMinimumSize(100, 150)
        bt.setMaximumSize(100, 150)
        self.ui.horizontalLayout_3.addWidget(bt)
    
    def clear(self):
        
        while self.ui.horizontalLayout_3.count():
            item = self.ui.horizontalLayout_3.takeAt(0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.horizontalLayout_3.removeWidget(widget)
                    widget.deleteLater()

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


