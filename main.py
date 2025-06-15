from PyQt5.QtWidgets import QApplication, QSizePolicy, QMainWindow, QStackedWidget, QWidget, QPushButton, QLabel, QGridLayout
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from services import Home_window
from authentication import Login_window, Register_window
import uvicorn
from api.main_api import app
import threading
from blackhole import Welcome_page

def start_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)

# class Welcome_window(QWidget):
#     def __init__(self, My_window):
#         super().__init__()
#         Vbox = QGridLayout(self)
        
#         Label = QLabel("ePass\nDiginal identification system", self)
#         Label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
#         Label.setStyleSheet("font-size: 25px; font-weight: bold; background-color: red; font-family: Georgia;")

#         Button_login = QPushButton("Log In", self)
#         Button_register = QPushButton("Register", self)
        
#         self.config_button(Button_login)
#         self.config_button(Button_register)

#         Button_login.clicked.connect(My_window.go_login)
#         Button_register.clicked.connect(My_window.go_register)

#         Vbox.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
#         Vbox.setSpacing(20)
#         Vbox.addWidget(Label, 0, 0, 1, 2)
#         Vbox.addWidget(Button_login, 1, 0)
#         Vbox.addWidget(Button_register, 1, 1)
#         self.setLayout(Vbox)

#     def config_button(self, button):
#         button.setStyleSheet("background-color: grey; color: white; font-size: 20px; font-family: Trebuchet MS;")
#         button.setMaximumWidth(250)
#         button.setFixedHeight(40)
#         button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

class Epass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Epass")
        self.setGeometry(610, 270, 700, 540)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setGeometry(0, 0, 700, 540)
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
            self.Login = Login_window(self)
            self.stack.addWidget(self.Login)
        self.stack.setCurrentWidget(self.Login)
    
    def go_register(self):
        if not self.Register:
            self.Register = Register_window(self)
            self.stack.addWidget(self.Register)
        self.stack.setCurrentWidget(self.Register)
        
    def go_home(self):
        if not self.Main:
            self.Main = Home_window()
            self.stack.addWidget(self.Main)
        self.stack.setCurrentWidget(self.Main)
    
class Welcome(Welcome_page):
    def __init__(self, epass):
        super().__init__()
        self.Login_btn.clicked.connect(epass.go_login)
        self.Register_btn.clicked.connect(epass.go_register)


if __name__ == "__main__":
    # api_thread = threading.Thread(target=start_api, daemon=True)
    # api_thread.start()

    application = QApplication(sys.argv)
    window = Epass()
    window.show()
    sys.exit(application.exec_())