from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout, QMessageBox, QDialog
from sqlalchemy.orm import Session
from PyQt5.QtCore import Qt
import requests

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

    def submit(self, go_home):
        try:
            data = {
                "username": self.user.text(),
                "password": self.password.text()
            }
            response = requests.post("http://127.0.0.1:8000/login", data=data)

            if response.status_code == 200:
                token = response.json()["token"]
                print("sucsseesss")
            else:
                QMessageBox.warning(self, "Failed", f"Login failed:\n{response.json()['detail']}")
            
            go_home()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")
        

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

    def submit(self, go_home, db: Session = None):
        try:
            data = {
                "pers_id": self.pers_id.text(),
                "username": self.user.text(),
                "password": self.password.text(),
                "r_password": self.r_password.text()
            }
            response = requests.post("http://127.0.0.1:8000/register", json=data)

            if response.status_code == 201:
                print("registered")
            else:
                QMessageBox.warning(self, "Failed", f"register failed:\n{response.json()['detail']}")
            
            go_home()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")