import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, QIcon

from WatchPageUi import Ui_Form

import Account
import Connection

class WatchC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user

        self.ui.addButton.clicked.connect(self.addMovie)
        self.ui.deleteButton.clicked.connect(self.removeMovie)

    def load(self, user):
        self.user = user

        for m in self.user.getWatchedList().getList():
            image = m.getImagePath()
            print(image)

            b = QPushButton()
            b.setMinimumSize(100, 150)
            b.setMaximumSize(100, 150)
            pixmap = QPixmap(image)

            enlarged_pixmap = pixmap.scaled(100, 150)
            b.setIcon(QIcon(enlarged_pixmap))
            b.setIconSize(enlarged_pixmap.size())
            self.ui.horizontalLayout_5.addWidget(b)
        
        for m in self.user.getWillWatchList().getList():
            image = m.getImagePath()
            print(image)

            b = QPushButton()
            b.setMinimumSize(100, 150)
            b.setMaximumSize(100, 150)
            pixmap = QPixmap(image)

            enlarged_pixmap = pixmap.scaled(100, 150)
            b.setIcon(QIcon(enlarged_pixmap))
            b.setIconSize(enlarged_pixmap.size())
            self.ui.horizontalLayout_4.addWidget(b)

        for m in self.user.getWatchingList().getList():
            image = m.getImagePath()
            print(image)

            b = QPushButton()
            b.setMinimumSize(100, 150)
            b.setMaximumSize(100, 150)
            pixmap = QPixmap(image)

            enlarged_pixmap = pixmap.scaled(100, 150)
            b.setIcon(QIcon(enlarged_pixmap))
            b.setIconSize(enlarged_pixmap.size())
            self.ui.horizontalLayout_3.addWidget(b)
    
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
    
    def addMovie(self):
        title = self.ui.searchLED.text()
        tmp = self.whichType()
        exist = self.isMovieExist(title)
        if tmp == False:
            self.ui.textArea.setPlainText("Invalid check box")
            return
        if exist == False:
            suggest_tmp = Account.Movie.getSuggestionFromTitle(title)
            self.ui.textArea.setPlainText("Movie Not Exist, Here Suggestion: ")

            for s in suggest_tmp:
                self.ui.textArea.appendPlainText(s)
            return
     
        m1 = Account.Movie(title)
        image = m1.getImagePath()
        print(image)

        b = QPushButton()
        b.setMinimumSize(100, 150)
        b.setMaximumSize(100, 150)
        pixmap = QPixmap(image)

        enlarged_pixmap = pixmap.scaled(100, 150)
        b.setIcon(QIcon(enlarged_pixmap))
        b.setIconSize(enlarged_pixmap.size())

        if (tmp == "watching"):
            self.ui.horizontalLayout_3.addWidget(b)
            self.user.getWatchingList().addMovie(m1)
        elif (tmp == "will watch"):
            self.ui.horizontalLayout_4.addWidget(b)
            self.user.getWillWatchList().addMovie(m1)
        elif (tmp == "watched"):
            self.ui.horizontalLayout_5.addWidget(b)
            self.user.getWatchedList().addMovie(m1)
        
        Connection.Connection.saveData()
    
    def isMovieExist(self, title):
        m1 = Account.Movie(title)
        tmp = Account.Movie.getSuggestionFromTitle(title)
        for t in tmp:
            if title == t:
                return True
            else:
                return False
      
    def removeMovie(self):
        title = self.ui.searchLED.text()

        type = self.whichType()

        if(type == False):
            self.ui.textArea.SetPlainText("No movie")
            print("type false")
        elif type == "watched":
            print("watched")
            i = self.user.getWatchedList().deleteMovie(title)
            print(i)
            item = self.ui.horizontalLayout_5.takeAt(i)
            if item is not None:
                widget = item.widget()
                if isinstance(widget, QPushButton):
                    self.ui.horizontalLayout_3.removeWidget(widget)
                    widget.deleteLater()
        elif type == "watching":
            i = self.user.getWatchingList().deleteMovie(title)
            print(i)
            item = self.ui.horizontalLayout_3.takeAt(i)
            if item is not None:
                widget = item.widget()
                if isinstance(widget, QPushButton):
                    self.ui.horizontalLayout_3.removeWidget(widget)
                    widget.deleteLater()
        elif type == "will watch":
            i = self.user.getWillWatchList().deleteMovie(title)
            print(i)
            item = self.ui.horizontalLayout_4.takeAt(i)
            if item is not None:
                widget = item.widget()
                if isinstance(widget, QPushButton):
                    self.ui.horizontalLayout_3.removeWidget(widget)
                    widget.deleteLater()
                    
        Connection.Connection.saveData()


    def clear(self):
        self.ui.searchLED.clear()
        self.ui.textArea.clear()
        self.ui.watchedCB.setChecked(False)
        self.ui.watchingCB.setChecked(False)
        self.ui.willwatchCB.setChecked(False)


        while self.ui.horizontalLayout_3.count()-1:
            item = self.ui.horizontalLayout_3.takeAt(1)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.horizontalLayout_3.removeWidget(widget)
                    widget.deleteLater()
        
        while self.ui.horizontalLayout_4.count()-1:
            item = self.ui.horizontalLayout_4.takeAt(1)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.horizontalLayout_4.removeWidget(widget)
                    widget.deleteLater()
        
        while self.ui.horizontalLayout_5.count()-1:
            item = self.ui.horizontalLayout_5.takeAt(1)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.horizontalLayout_5.removeWidget(widget)
                    widget.deleteLater()
