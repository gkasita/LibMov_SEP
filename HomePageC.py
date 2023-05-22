import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from HomePageUi import Ui_Form
from PySide6.QtGui import QPixmap, QIcon

import Connection
import LSCode

#lineedit, pushButton, pf_label
class HomePageC(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.retrieveProfile)
    
    def retrieveProfile(self):
        while self.ui.verticalLayout_2.count()-1:
            item = self.ui.verticalLayout_2.takeAt(1)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.verticalLayout_2.removeWidget(widget)
                    widget.deleteLater()

        username = self.ui.lineEdit.text()

        tmp = LSCode.LS.isUsernameExist(username)

        if(tmp == False):
            self.ui.pf_label.setText("username doesn't exist")
            return
        self.user = Connection.Connection.getUser(username)
        self.ui.pf_label.setText(username)
        
        for r in self.user.getReviewList().getList():
            title = r.getMovie().getTitle()
            star_rating = r.getStarRating()
            review_text = r.getReviewText()

            image = r.getMovie().getImagePath()

            widget = QWidget(self.ui.scrollAreaWidgetContents)
            widget.setObjectName(u"widget")
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
            TitleLB.setText(title)

            reviewArea = QPlainTextEdit(widget)
            reviewArea.setObjectName(u"reviewArea")
            reviewArea.setGeometry(QRect(360, 40, 421, 161))
            reviewArea.setStyleSheet(u"background-color: rgb(232, 232, 232);")
            reviewArea.setPlainText(review_text)

            movieLB = QLabel(widget)
            movieLB.setObjectName(u"movieLB")
            movieLB.setGeometry(QRect(160, 50, 181, 111))
            movieLB.setText("Movie ID: " + str(r.getMovie().getMovieId()) + "\n" + "Genre: " + str(r.getMovie().getGenre()) + "\n" + "Released Year: " + str(r.getMovie().getReleasedYear())+ "\n" + "Posted on: " + str(r.getDateTime()))

            starratingLED = QLineEdit(widget)
            starratingLED.setObjectName(u"starratingLED")
            starratingLED.setGeometry(QRect(240, 170, 113, 21))
            starratingLED.setStyleSheet(u"background-color: rgb(232, 232, 232);")
            starratingLED.setText(str(star_rating))
            label_3 = QLabel(widget)
            label_3.setObjectName(u"label_3")
            label_3.setGeometry(QRect(160, 170, 71, 16))
            label_3.setText("Star Rating: ")

            self.ui.verticalLayout_2.addWidget(widget)
    
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.pf_label.clear()

        while self.ui.verticalLayout_2.count()-1:
            item = self.ui.verticalLayout_2.takeAt(1)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    self.ui.verticalLayout_2.removeWidget(widget)
                    widget.deleteLater()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomePageC()
    w.show()
    sys.exit(app.exec_())




    