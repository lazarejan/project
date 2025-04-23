from database import get_session, Citizens, Account, ID_card, Passport, Car_license
from PyQt5.QtWidgets import QApplication, QSizePolicy, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QHBoxLayout, QMessageBox, QDialog, QGridLayout
import sys
from sqlalchemy.orm import Session
from PyQt5.QtCore import Qt
from auth import reg_requirements

class Welcome_window(QWidget):
    def __init__(self, My_window):
        super().__init__()
        Vbox = QGridLayout(self)
        
        Label = QLabel("ePass\nDiginal identification system", self)
        Label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        Label.setStyleSheet("font-size: 25px; font-weight: bold; background-color: red; font-family: Georgia;")

        Button_login = QPushButton("Log In", self)
        Button_register = QPushButton("Register", self)
        
        self.config_button(Button_login)
        self.config_button(Button_register)

        Button_login.clicked.connect(My_window.go_login)
        Button_register.clicked.connect(My_window.go_register)

        Vbox.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        Vbox.setSpacing(20)
        Vbox.addWidget(Label, 0, 0, 1, 2)
        Vbox.addWidget(Button_login, 1, 0)
        Vbox.addWidget(Button_register, 1, 1)
        self.setLayout(Vbox)

    def config_button(self, button):
        button.setStyleSheet("background-color: grey; color: white; font-size: 20px; font-family: Trebuchet MS;")
        button.setMaximumWidth(250)
        button.setFixedHeight(40)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

class Login_window(QDialog):
    def __init__(self, My_window):
        super().__init__()

        self.user = QLineEdit()
        self.password = QLineEdit()
        Pass_box = QHBoxLayout()
        self.user.setPlaceholderText("Enter your username")        
        self.password.setPlaceholderText("Enter your password")
        self.password.setEchoMode(QLineEdit.Password)
        self.user.setFixedSize(300, 30)
        self.password.setFixedSize(300, 30)
        self.user.setStyleSheet("font-size: 15px")

        self.toggle_button = QPushButton()
        self.toggle_button.setFixedWidth(30)
        self.toggle_button.setText("👁️") 
        self.toggle_button.setCheckable(True)
        self.toggle_button.clicked.connect(self.toggle_password_visibility)

        Pass_box.addWidget(self.password)
        Pass_box.addWidget(self.toggle_button)

        Submit = QPushButton("Sign Up", self)
        Submit.setFixedSize(120, 30)
        Submit.clicked.connect(lambda: self.submit(My_window.go_home))

        Back_button = QPushButton("<", self)
        Back_button.setGeometry(10, 10, 30, 30)
        Back_button.clicked.connect(My_window.go_welcome)

        Form = QVBoxLayout()
        Form.addWidget(self.user)
        Form.addLayout(Pass_box)
        Form.addWidget(Submit, alignment=Qt.AlignCenter)
        Form.setAlignment(Qt.AlignCenter)

        self.setLayout(Form)

    @get_session
    def submit(self, go_home, db: Session = None):
        account = db.query(Account).filter(Account.username == self.user.text()).first()

        if not account:
            QMessageBox.warning(self, "Verification", "User is not registered")
            return
        if account.password != self.password.text():
            QMessageBox.warning(self, "Verification", "Password is incorrect")
            return
        
        go_home()
    
    def toggle_password_visibility(self):
        if self.toggle_button.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)  # Show password
        else:
            self.password.setEchoMode(QLineEdit.Password)  # Hide password
            
    
class Register_window(QDialog):
    """
    Registration window for new users.
    
    """
    def __init__(self, My_window):
        super().__init__()
        
        self.pers_id = QLineEdit()
        self.user = QLineEdit()
        self.password = QLineEdit()
        self.r_password = QLineEdit()
        self.pers_id.setPlaceholderText("Enter your personal ID")
        self.user.setPlaceholderText("Enter your username")
        self.password.setPlaceholderText("Enter your password")
        self.r_password.setPlaceholderText("Repeat your password")
        self.pers_id.setFixedSize(300, 30)
        self.user.setFixedSize(300, 30)
        self.password.setFixedSize(300, 30)
        self.r_password.setFixedSize(300, 30)

        Submit = QPushButton("Sign Up", self)
        Submit.setFixedSize(120, 30)
        # lambdati gadawyda imitor chveulebriv roca vadzlevdit arguments mag dros db-shi difoltad tavisiTsvamda arguments (false) a 
        # da mere roca get_session cdilobda bd-stvis argumentis micemas erors agdebda.
        Submit.clicked.connect(lambda: self.submit(My_window.go_home))

        Back_button = QPushButton("<", self)
        Back_button.setGeometry(10, 10, 30, 30)
        Back_button.clicked.connect(My_window.go_welcome)

        Form = QVBoxLayout()
        Form.addWidget(self.pers_id)
        Form.addWidget(self.user)
        Form.addWidget(self.password)
        Form.addWidget(self.r_password)
        Form.addWidget(Submit, alignment=Qt.AlignCenter)
        Form.setAlignment(Qt.AlignCenter)

        self.setLayout(Form)

    @get_session
    @reg_requirements
    def submit(self, go_home, db: Session = None):
        citizen = db.query(Citizens).filter(Citizens.personal_id == self.pers_id.text()).first()
        is_registered = db.query(Account).filter( Account.personal_id == self.pers_id.text()).first()
        username_taken = db.query(Account).filter(Account.username == self.user.text()).first()

        if is_registered:
            QMessageBox.warning(self, "Registrasion error", "Person is already Registered")
            return
        if username_taken:
            QMessageBox.warning(self, "Username is taken", "Username is already taken, please choose another one")
            return
        if not citizen:
            QMessageBox.warning(self, "Error 404", "Citizen not found")
            return
        
        add_account = Account(username=self.user.text(), password=self.password.text(), personal_id=citizen.personal_id)
        db.add(add_account)

        go_home()

class Home_window(QWidget):
    def __init__(self, My_window):
        super().__init__()
        self.setWindowTitle("Home")
        Btn = QPushButton("Logout", self)
        Btn.clicked.connect(My_window.go_welcome)

class My_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first window")
        self.setGeometry(960-350, 270, 700, 540)
        self.initUI()
    
    def initUI(self):
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)
        self.stack.setGeometry(0, 0, 700, 540)
        Login = Login_window(self)
        Home = Home_window(self)
        Welcome = Welcome_window(self)
        Register = Register_window(self)

        self.stack.addWidget(Welcome) # index: 0
        self.stack.addWidget(Login) # index: 1
        self.stack.addWidget(Register) # index: 2
        self.stack.addWidget(Home) # index: 3

        self.go_welcome()

    def go_welcome(self):
        self.stack.setCurrentIndex(0)    
    def go_login(self):
        self.stack.setCurrentIndex(1)
    def go_register(self):
        self.stack.setCurrentIndex(2)
    def go_home(self):
        self.stack.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_window()
    window.show()
    sys.exit(app.exec_())