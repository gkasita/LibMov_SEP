import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, QIcon

from ReviewPageUi import Ui_Form

import Account
import Connection

#searchLED, addButton, editButton, deleteButton, ratingSPB, textArea
class ReviewC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user

        self.ui.addButton.clicked.connect(self.addReviewUi)
        self.ui.deleteButton.clicked.connect(self.removeReview)
        self.ui.editButton.clicked.connect(self.modifyReview)
        self.ui.saveButton.clicked.connect(self.saveReview)
    
    def load(self, user):
        self.user = user

        for r in self.user.getReviewList().getList():
            self.addReview(r.getMovie().getTitle(), r.getStarRating(), r.getReviewText(), "notui")
    
    def isMovieExist(self, title):
        m1 = Account.Movie(title)
        tmp = Account.Movie.getSuggestionFromTitle(title)
        for t in tmp:
            if title == t:
                return True
            else:
                return False

    def removeReview(self):
        self.ui.label_2.setText(" ")
        title = self.ui.searchLED.text()
        tmp = self.user.getReviewList()

        i = tmp.deleteMovie(title)
        if i is not None:
            item = self.ui.verticalLayout.takeAt(i+1)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.verticalLayout.removeWidget(widget)
                    widget.deleteLater()
        
        Connection.Connection.saveData()


    def modifyReview(self):
        title = self.ui.searchLED.text()

        tmp = self.user.getReviewList().getList()

        for r in tmp:
            if r.getMovie().getTitle() == title:
                self.ui.ratingSPB.setValue(r.getStarRating())
                self.ui.textArea.setPlainText(r.getReviewText())
                return
            else:
                self.ui.label_2.setText("No Review of this movie exists")
        
        return False
    
    def saveReview(self):
        self.ui.label_2.setText(" ")
        title = self.ui.searchLED.text()
        tmp = self.user.getReviewList().getList()

        bool = False

        for r in tmp:
            if r.getMovie().getTitle() == title:
                bool = True
            else:
                self.ui.label_2.setText("No Review of this movie exists")
        
        if(bool):    
            self.removeReview()
            self.addReviewUi()
        
    def clear(self):
        self.ui.searchLED.clear()
        self.ui.textArea.clear()
        self.ui.label_2.setText(" ")

        while self.ui.verticalLayout.count()-2:
            item = self.ui.verticalLayout.takeAt(2)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.verticalLayout.removeWidget(widget)
                    widget.deleteLater()
    
    def addReviewUi(self):
        self.ui.label_2.setText(" ")
        title = self.ui.searchLED.text()
        rating = self.ui.ratingSPB.value()
        review = self.ui.textArea.toPlainText()

        self.addReview(title, rating, review, "ui")

    def addReview(self, t, rt, rv, type):
        title = t
        rating = rt
        review = rv
        type = type

        if(self.isMovieExist(title)== False):
            self.ui.label_2.setText("movie does not exist")
            return
        
        m1 = Account.Movie(title)
        if(type=="ui"):
            r1 = Account.ReviewMovie(m1, review, rating)

            self.user.getReviewList().addMovie(r1)
            Connection.Connection.saveData()

        r1 = Account.ReviewMovie(m1, review, rating)
        image = m1.getImagePath()

        widget = QWidget(self.ui.scrollAreaWidgetContents)
        widget.setObjectName(u"widget_2")
        widget.setMinimumSize(QSize(800, 220))
        widget.setMaximumSize(QSize(800, 220))
        widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius: 20px")
        pushButton_3 = QPushButton(widget)
        pushButton_3.setObjectName(u"pushButton_3")
        pushButton_3.setGeometry(QRect(30, 40, 115, 170))
        pushButton_3.setMinimumSize(QSize(115, 170))
        pushButton_3.setMaximumSize(QSize(115, 170))
        pixmap = QPixmap(image)

        enlarged_pixmap = pixmap.scaled(100, 150)
        pushButton_3.setIcon(QIcon(enlarged_pixmap))
        pushButton_3.setIconSize(enlarged_pixmap.size())
        
        TitleLB = QLabel(widget)
        TitleLB.setObjectName(u"TitleLB")
        TitleLB.setGeometry(QRect(40, 20, 241, 16))
        TitleLB.setText(m1.getTitle())

        reviewArea = QPlainTextEdit(widget)
        reviewArea.setObjectName(u"reviewArea")
        reviewArea.setGeometry(QRect(360, 40, 421, 161))
        reviewArea.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        reviewArea.setPlainText(review)

        movieLB = QLabel(widget)
        movieLB.setObjectName(u"movieLB")
        movieLB.setGeometry(QRect(160, 50, 181, 111))
        movieLB.setText("Movie ID: " + str(m1.getMovieId()) + "\n" + "Genre: " + str(m1.getGenre()) + "\n" + "Released Year: " + str(m1.getReleasedYear()) + "\n" + "Posted on: " + str(r1.getDateTime()))

        starratingLED = QLineEdit(widget)
        starratingLED.setObjectName(u"starratingLED")
        starratingLED.setGeometry(QRect(240, 170, 113, 21))
        starratingLED.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        starratingLED.setText(str(rating))
        label_3 = QLabel(widget)
        label_3.setObjectName(u"label_3")
        label_3.setGeometry(QRect(160, 170, 71, 16))
        label_3.setText("Star Rating: ")

        self.ui.verticalLayout.addWidget(widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ReviewC()
    w.show()
    sys.exit(app.exec_())
