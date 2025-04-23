from PyQt5.QtWidgets import QMessageBox
def reg_requirements(func):
    def wrapper(self, *args, **kwargs):
        username = self.user.text()
        pas = self.password.text()
        r_pas = self.r_password.text()
        error_msg = []

        if username == ("" or " " or None):
            error_msg.append(" * Username cannot be empty")
        if len(username) < 5 or len(username) > 20:
            error_msg.append(" * Username length should be 5-20 characters")
        
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
            QMessageBox.warning(self, "Verification", "\n".join(error_msg))
            return
        
        return func(self, *args, **kwargs)

    return wrapper