from database import get_session, Citizens, Account, ID_card, Passport, Car_license
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QHBoxLayout, QMessageBox, QDialog
import sys
from sqlalchemy.orm import Session

class Login_window(QDialog):
    def __init__(self, go_home):
        super().__init__()
        
        self.user = QLineEdit()
        self.password = QLineEdit()

        Submit = QPushButton("Log In", self)
        Submit.clicked.connect(go_home)
        # lambdati gadawyda imitor chveulebriv roca vadzlevdit arguments mag dros db-shi difoltad tavisiTsvamda arguments (false) a 
        # da mere roca get_session cdilobda bd-stvis argumentis micemas erors agdebda.
        Submit.clicked.connect(lambda: self.submit())
        Form = QFormLayout()
        Form.addRow(QLabel("Email:"), self.user)
        Form.addRow(QLabel("Password:"), self.password)

        self.setLayout(Form)

    # ideashi es punqcia mushaobs mara arasworadaa funqcionali da chaaswore

    # @authorisasionrequirments like: first letter should be capital, length should be 8-20, etc.
    @get_session
    def submit(self, db: Session = None):
        users = db.query(Citizens).filter(Citizens.personal_id == self.user.text()).first()

        if not users:
            raise Exception("User not found")
        
        new_account = Account(username=self.user.text(), password=self.password.text(), personal_id=users.personal_id)

        db.add(new_account)

        print(users)
        print(self, db)

class Home_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        btn = QPushButton("Logout", self)
        # btn.clicked.connect()

class My_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first window")
        self.setGeometry(960-350, 270, 700, 540)
        self.initUI()
    
    def initUI(self):
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)
        self.stack.setGeometry(0, 0, 960, 540)

        self.login = Login_window(self.go_home)
        self.home = Home_window()

        self.stack.addWidget(self.login) # index: 0
        self.stack.addWidget(self.home) # index: 1

        self.stack.setCurrentIndex(0)
    
    def go_home(self):
        self.stack.setCurrentIndex(1)
        print("Login successful")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())