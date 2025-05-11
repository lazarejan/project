from PyQt5.QtWidgets import QApplication, QSizePolicy, QMainWindow, QStackedWidget, QWidget, QPushButton, QLabel, QGridLayout
import sys
from PyQt5.QtCore import Qt
from services import Passport_window, Home_window
from auth import Login_window, Register_window

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

class My_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first window")
        self.setGeometry(610, 270, 700, 540)
        self.initUI()
    
    def initUI(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setGeometry(0, 0, 700, 540)
        Welcome = Welcome_window(self)

        self.stack.addWidget(Welcome) # index: 0
        self.login_window = None
        self.register_window = None
        self.home_window = None

        self.go_welcome()

    def go_welcome(self):
        self.stack.setCurrentIndex(0)    
        
    def go_login(self):
        if not self.login_window:
            self.login_window = Login_window(self)
            self.stack.addWidget(self.login_window)
        self.stack.setCurrentWidget(self.login_window)
    
    def go_register(self):
        if not self.register_window:
            self.register_window = Register_window(self)
            self.stack.addWidget(self.register_window)
        self.stack.setCurrentWidget(self.register_window)
        
    def go_home(self, user):
        if not self.home_window:
            self.home_window = Home_window(self, user)
            self.stack.addWidget(self.home_window)
        self.stack.setCurrentWidget(self.home_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_window()
    window.show()
    sys.exit(app.exec_())