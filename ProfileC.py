import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PySide6 import QtCharts

from ProfilePageUi_ui import Ui_Form
import Account, Connection

class ProfileC(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user
        self.ui.button.clicked.connect(self.updatePassword)
    
    def load(self, user):
        self.user = user
        self.ui.label.setText(f"Welcome, {self.user.getUsername()}!")
        self.ui.label.setGeometry(QRect(500,200, 200, 100))

        self.ui.label_2.setText(f"{self.user.getWatchedList().getTotalMovie()}")
        self.ui.label_3.setText(f"{self.user.getWatchedList().getTotalMovie()}")
        self.ui.label_4.setText(f"{self.user.getWatchedList().getTotalMovie()}")



    def updatePassword(self):
        reply = QMessageBox.question(
            self, "Confirmation", "Are you sure you want to change your password?", 
            QMessageBox.Yes | QMessageBox.No
        )
       
        if reply == QMessageBox.Yes:
            password, ok = QInputDialog.getText(
                self, "Change Password", "Enter your new password:", QLineEdit.Password
            )
            if ok and password.strip():
                confirmed_password, ok = QInputDialog.getText(
                 self, "Change Password", "Confirm your new password:", QLineEdit.Password
                )
                if ok and confirmed_password.strip():
                    self.user.setPassword(password, confirmed_password)
                    Connection.Connection.saveData()  # Save the updated user data
                    QMessageBox.information(self, "Success", "Password changed successfully!")
                else:
                    QMessageBox.warning(self, "Error", "Invalid confirmed password!")
            else:
                QMessageBox.warning(self, "Error", "Invalid password!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ProfileC()
    w.show()
    sys.exit(app.exec_())