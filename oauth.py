from PyQt5.QtWidgets import QMessageBox

def reg_requirements(func):
    def wrapper(self, *args, **kwargs):
        username = self.user.text()
        pas = self.password.text()
        r_pas = self.r_password.text()
        error_msg = []

        if username == (""):
            error_msg.append(" * Username cannot be empty")
        if len(username) < 5 or len(username) > 20:
            error_msg.append(" * Username length should be 5-20 characters")
        if " " in username:
            error_msg.append(" * Username cannot contain spaces")
        
        if pas == ("" or " " or None):
            error_msg.append(" * Password cannot be empty")
        if len(pas) < 8 or len(pas) > 20:
            error_msg.append(" * Password length should be 8-20 characters")
        if not any(char.isdigit() for char in pas):
            error_msg.append(" * Password should contain at least one digit")
        if not any(char.isupper() for char in pas):
            error_msg.append(" * Password should contain at least one uppercase letter")
        if pas != r_pas:
            error_msg.append(" * Passwords do not match")

        if error_msg:
            QMessageBox.warning(self, "Pattern Error", "\n".join(error_msg))
            return
        
        return func(self, *args, **kwargs)

    return wrapper

def encrypt(password: str) -> str:
    """
    Encrypts the password using hashing algorithm.
    """

    len_ = len(password)
    for i, l in enumerate(password):
        password = password[:i] + chr(ord(l) - len_) + password[i+1:]
    return password

def decrypt(password: str) -> str:
    """
    Decrypts the password using hashing algorithm.
    """

    len_ = len(password)
    for i, l in enumerate(password):
        password = password[:i] + chr(ord(l) + len_) + password[i+1:]
    return password

class Curr_user:
    def __init__(self, account):
        self.account = account
        self.personal_id = account.personal_id
        self.username = account.username
        self.password = account.password
