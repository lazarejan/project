from database import get_session, Citizens, Account, ID_card, Passport, Car_license
from PyQt5.QtWidgets import QApplication, QSizePolicy, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QHBoxLayout, QMessageBox, QDialog, QGridLayout
from auth import curr_user
from sqlalchemy.orm import Session

class Home_window(QWidget):
    def __init__(self, My_window):
        super().__init__()
        self.setWindowTitle("Home")
        Passport_button = QPushButton("Passport", self)
        Passport_button.clicked.connect(My_window.go_passport)
        Btn = QPushButton("Logout", self)
        Btn.clicked.connect(My_window.go_welcome)

class Passport_window(QWidget):
    def __init__(self, My_window):
        super().__init__()
        print("Passport window")
        self.passport_id = self.fetch_data()

    @get_session
    def fetch_data(self, curr = curr_user, db: Session = None):
        user = db.query(Account).filter(Account.username == curr.account.username).first()
        return user
        