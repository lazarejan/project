from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLineEdit ,QMessageBox
import sys
from services import Home_window
import uvicorn
from api.main_api import app
import threading
from blackhole import Welcome_page, Login_page, Register_page, AppState
import requests

def start_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)


class Epass(QMainWindow):
    """
    Main class in the application
    
    This is responsible for managing and activating all the pages(widgets): Welcome, Login, Register, Main pages(classes) 
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Epass")
        self.setGeometry(610, 270, 800, 600)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setGeometry(0, 0, 800, 600)
        self.Welcome = Welcome(self)

        self.stack.addWidget(self.Welcome)
        self.Login = None
        self.Register = None
        self.Main = None

        self.go_welcome()

    def go_welcome(self):
        self.stack.setCurrentWidget(self.Welcome)    
        
    def go_login(self):
        if not self.Login:
            self.Login = Login(self)
            self.stack.addWidget(self.Login)
        self.stack.setCurrentWidget(self.Login)
    
    def go_register(self):
        if not self.Register:
            self.Register = Register(self)
            self.stack.addWidget(self.Register)
        self.stack.setCurrentWidget(self.Register)
        
    def go_home(self):
        if not self.Main:
            self.Main = Home_window()
            self.stack.addWidget(self.Main)
        self.stack.setCurrentWidget(self.Main)
    
class Welcome(Welcome_page):
    """
    First page
    """
    def __init__(self, epass):
        super().__init__()
        self.login_btn.clicked.connect(epass.go_login)
        self.register_btn.clicked.connect(epass.go_register)

class Login(Login_page):
    """
    Login page for logging in an existing account
    """
    def __init__(self, epass):
        super().__init__()
        self.back_btn.clicked.connect(epass.go_welcome)
        self.login_btn.clicked.connect(lambda: self.login__(self.personal_num_inp.text(), self.password_inp.text(), epass))
        self.echo_toggle_btn.setCheckable(True)
        self.echo_toggle_btn.clicked.connect(self.echo_toggle__)
    
    def login__(self, pers_num, passwd, epass):
        try:
            data= {
                "username": pers_num,
                "password": passwd,
            }

            response = requests.post("http://127.0.0.1:8000/login", data=data)

            if response.status_code == 200:
                AppState.token = response.json()["token"]
                epass.go_home()
                print("loged in")
            else:
                QMessageBox.warning(self, "Failed", f"Login failed:\nusername or password is incorrect")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")
    
    def echo_toggle__(self):
        if self.echo_toggle_btn.isChecked():
            self.password_inp.setEchoMode(QLineEdit.Normal)  # Show password
        else:
            self.password_inp.setEchoMode(QLineEdit.Password)  # Hide password
    
class Register(Register_page):
    """
    Registration page for new users to create their account.
    
    """
    def __init__(self, epass):
        super().__init__()
        self.back_btn.clicked.connect(epass.go_welcome)
        self.register_btn.clicked.connect(lambda: self.register__(epass))
    
    def register__(self, epass):
        try:
            data = {
                "pers_id": self.personal_num_inp.text(),
                "username": self.username_inp.text(),
                "password": self.password_inp.text(),
                "r_password": self.rpassword_inp.text()
            }
            response = requests.post("http://127.0.0.1:8000/register", json=data)

            if response.status_code == 201:
                AppState.token = response.json()["token"]
                epass.go_home()
                print("registered")
            else:
                QMessageBox.warning(self, "Failed", f"register failed:\n{response.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

if __name__ == "__main__":
    # api_thread = threading.Thread(target=start_api, daemon=True)
    # api_thread.start()

    application = QApplication(sys.argv)
    window = Epass()
    window.show()
    sys.exit(application.exec_())