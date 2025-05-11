from database import get_session, Citizens, Account
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout, QMessageBox, QDialog
from sqlalchemy.orm import Session
from PyQt5.QtCore import Qt
from oauth import reg_requirements, encrypt, decrypt, Curr_user

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
        if decrypt(account.password) != self.password.text():
            QMessageBox.warning(self, "Verification", "Password is incorrect")
            return
        
        # current user variable
        curr_user = Curr_user(account)

        go_home(curr_user)
    
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
        is_registered = db.query(Account).filter(Account.personal_id == self.pers_id.text()).first()
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
        passwrd = encrypt(self.password.text())

        add_account = Account(username=self.user.text(), password=passwrd, personal_id=citizen.personal_id)
        
        # current user variable
        curr_user = Curr_user(add_account)
        
        db.add(add_account)
        go_home(curr_user)

