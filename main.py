from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLineEdit ,QMessageBox
import sys
from PyQt5 import QtWidgets
import uvicorn
from api.main_api import app
import threading
from blackhole import Main_page, Welcome_page, Login_page, Register_page, AppState, Border_guard_page, Police_page, Ambassador_page
import requests
from PyQt5.QtCore import Qt

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
        self.setGeometry(460, 140, 1000, 800)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setGeometry(0, 0, 800, 600)
        self.Welcome = Welcome(self)

        self.stack.addWidget(self.Welcome)
        self.Login = None
        self.Register = None
        self.Main = None
        self.Border_guard = None
        self.Police = None
        self.Ambassador = None

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
        
    def go_main(self):
        if not self.Main:
            self.Main = Main(self)
            self.stack.addWidget(self.Main)
        self.stack.setCurrentWidget(self.Main)
    
    def go_border_guard(self):
        if not self.Border_guard:
            self.Border_guard = Border_guard(self)
            self.stack.addWidget(self.Border_guard)
        self.stack.setCurrentWidget(self.Border_guard)

    def go_police(self):
        if not self.Police:
            self.Police = Police(self)
            self.stack.addWidget(self.Police)
        self.stack.setCurrentWidget(self.Police)
    
    def go_ambassador(self):
        if not self.Ambassador:
            self.Ambassador = Ambassador(self)
            self.stack.addWidget(self.Ambassador)
        self.stack.setCurrentWidget(self.Ambassador)

    def log_out(self):
        self.Main = None
        self.Police = None
        self.Border_guard = None
        self.Ambassador = None
        self.stack.removeWidget(self.Main)
        self.stack.removeWidget(self.Police)
        self.stack.removeWidget(self.Border_guard)
        self.stack.removeWidget(self.Ambassador)
    
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
        self.login_btn.clicked.connect(lambda: self.login__(self.username_inp.text(), self.password_inp.text(), epass))
        self.echo_toggle_btn.setCheckable(True)
        self.echo_toggle_btn.clicked.connect(self.echo_toggle__)    

    def login__(self, username, passwd, epass):
        try:
            data= {
                "username": username,
                "password": passwd,
            }

            response = requests.post("http://127.0.0.1:8000/login", data=data)

            if response.status_code == 200:
                AppState.token = response.json()["token"]
                is_special = response.json()["is_special"]
                if is_special == "border_guard":
                    epass.go_border_guard()
                elif is_special == "police":
                    epass.go_police()
                elif is_special == "ambassador":
                    epass.go_ambassador()
                else:
                    epass.go_main()
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
                epass.go_main()
            else:
                QMessageBox.warning(self, "Failed", f"register failed:\n{response.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

class Universal_methods():
    """
    Universal methods which are user by various classes
    """
    def logout(self, epass):
        try:
            headers = {
                "Authorization": f"Bearer {AppState.token}"
            }

            logout = requests.post("http://127.0.0.1:8000/logout", headers=headers)
            
            if logout.status_code == 200:
                AppState.token = None
                epass.go_welcome()
                epass.log_out()
            else:
                QMessageBox.critical(self, "Failed", f"Log out failed:\n{logout.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")
    
    def update_search_scroll(self, people, status):
        for i in reversed(range(self.scroll_grid.count())):
            widget = self.scroll_grid.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        if status == 404:
            self.scroll_grid.addWidget(QtWidgets.QLabel("Users not found"), alignment=Qt.AlignCenter)

        else:
            for p in people:
                lay = QtWidgets.QHBoxLayout()
                lay.setContentsMargins(11, 0, 11, 0)
                lay.setSpacing(20)
                
                lay.addWidget(QtWidgets.QLabel(f"პირადი ნომ:  {p["personal_id"]}\nსახელი/გვარი:  {p["first_name"]+" "+p["last_name"]}\nმისამართი:  {p['address']}{f"\nმანქანა(ები):  {"\n".join((f"{x["brand"]}[{x["car_id"]}]" for x in p["car"]))}" if p["car"] != [] else ""}"))
                lay.addWidget(QtWidgets.QLabel(f"ჯარიმების რაოდენობა:  {p["fine_count"]}"))
                lay.addWidget(QtWidgets.QLabel(f"ვიზები:  {"\n".join((f"ქვ:{x["country"]} ტპ:{x["type"]} სტს:{x["status"]}" for x in p["visa"]))}"))
                lay.addWidget(QtWidgets.QLabel(f"სსზღ. ბეჭედი:  {"\n".join((f"ლოკ: {x["location"]} მიმ: {x["direction"]}  დრო: {x["timestamp"]}" for x in p["borderstamp"]))}"))
                
                container = QtWidgets.QFrame()
                container.setLayout(lay)

                self.scroll_grid.addWidget(container)        

    def search(self):
        try:
            response = requests.get("http://127.0.0.1:8000/data_fetch/search", params={"search": self.search_bar.text()})
            if response.status_code == 200 or response.status_code == 404:
                return self.update_search_scroll(response.json(), response.status_code)
            else:
                QMessageBox.critical(self, "Failed", f"search failed:\n{response.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

class Main(Main_page, Universal_methods):
    """
    
    """
    def __init__(self, epass):
        super().__init__()
        self.logout_btn.clicked.connect(lambda: self.logout(epass))
        self.data = self.data_fetch__()
        self.updateUi__()

    def updateUi__(self):
        user = self.data["user"]

        self.id_name.setText(f"სახელი:  {user["first_name"]}")
        self.car_name.setText(f"სახელი:  {user["first_name"]}")
        self.pass_name.setText(f"სახელი:  {user["first_name"]}")

        self.id_lname.setText(f"გვარი:  {user["last_name"]}")
        self.car_lname.setText(f"გვარი:  {user["last_name"]}")
        self.pass_lname.setText(f"გვარი:  {user["last_name"]}")

        self.id_cit_sex_bdate.setText(f"მოქ:  GEO   სქესი:  {user["sex"]}    დაბ. თარიღი:  {user["birth_date"]}")
        self.pass_cit_sex_bdate.setText(f"მოქ:  GEO   სქესი:  {user["sex"]}    დაბ. თარიღი:  {user["birth_date"]}")

        self.id_personal_num.setText(f"პირადი ნომ:  {user["personal_id"]}")
        self.pass_personal_num.setText(f"პირადი ნომ:  {user["personal_id"]}")

        self.id_nomeri.setText(f"ბარათის №:  {user["id_card"]["card_id"]}")
        self.passport_nomeri.setText(f"პასპორტის №:  {user["passport"]["passport_id"]}")

        self.id_date.setText(f"გაც. თარიღი:  {user["id_card"]["issue_date"]}    მოქ. ვადა:  {user["id_card"]["expiration_date"]}")
        self.pass_date.setText(f"გაც. თარიღი:  {user["passport"]["issue_date"]}    მოქ. ვადა:  {user["passport"]["expiration_date"]}")
        
        if user["car_license"]:
            self.car_date.setText(f"გაც. თარიღი:  {user["car_license"]["issue_date"]}    მოქ. ვადა:  {user["car_license"]["expiration_date"]}")
            self.car_cit_sex_bdate.setText(f"მოქ:  GEO   სქესი:  {user["sex"]}    დაბ. თარიღი:  {user["birth_date"]}")
            self.car_personal_num.setText(f"პირადი ნომ:  {user["personal_id"]}")
            self.car_license_nomeri.setText(f"მოწმობის №:  {user["car_license"]["car_license_id"]}")
        else:
            self.tab.removeTab(2)

        if self.data["fine_list"]:
            self.update_fine__(self.data["fine_list"])
        
        if self.data["visa_list"]:
            self.update_visa__(self.data["visa_list"])
        
        if self.data["borderstamp_list"]:
            self.update_borderstamp__(self.data["borderstamp_list"])

        if self.data["car_list"]:
            self.update_car__(self.data["car_list"])
    
    def update_car__(self, data):
        for i in reversed(range(self.car_content.count())):
            widget = self.car_content.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        for car in data:
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(5, 10, 5, 10)
            layout.setSpacing(10)
            id_label = QtWidgets.QLabel(f"მანქანის ID: {car['car_id']}")
            brand_label = QtWidgets.QLabel(f"ბრენდი: {car['brand']}")
            model_lab = QtWidgets.QLabel(f"მოდელი: {car['model']}")
            
            layout.addWidget(id_label)
            layout.addWidget(brand_label)
            layout.addWidget(model_lab)

            
            container = QtWidgets.QFrame()
            container.setLayout(layout)

            container.setStyleSheet("""
                QFrame {
                    background-color: rgba(240, 240, 240);
                    border-radius: 5px;
                }
            """)
            self.car_content.addWidget(container)

    def update_borderstamp__(self, data):
        for i in reversed(range(self.borderstamp_content.count())):
            widget = self.borderstamp_content.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
            
        for borderstamp in data:
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(5, 10, 5, 10)
            layout.setSpacing(10)
            id_label = QtWidgets.QLabel(f"სასაზღვრო ბეჭდის ID: {borderstamp['stamp_id']}")
            country_direction_label = QtWidgets.QLabel(f"ქვეყანა: {borderstamp['location']}\nმიმართულება: {borderstamp['direction']}")
            date_lab = QtWidgets.QLabel(f"თარიღი: {borderstamp['timestamp']}")
            
            layout.addWidget(id_label)
            layout.addWidget(country_direction_label)
            layout.addWidget(date_lab)

            layout.setStretch(0, 1)
            layout.setStretch(1, 1)
            
            container = QtWidgets.QFrame()
            container.setLayout(layout)

            container.setStyleSheet("""
                QFrame {
                    background-color: rgba(240, 240, 240);
                    border-radius: 5px;
                }
            """)
            self.borderstamp_content.addWidget(container)

    def update_visa__(self, data):
        for i in reversed(range(self.visa_content.count())):
            widget = self.visa_content.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
            
        for visa in data:
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(5, 10, 5, 10)
            layout.setSpacing(10)
            id_status_label = QtWidgets.QLabel(f"ვიზის ID: {visa['visa_id']}\nსტატუსი: {visa['status']}")
            country_type_label = QtWidgets.QLabel(f"ქვეყანა: {visa['country']}\nტიპი: {visa['type']}")
            dates_label = QtWidgets.QLabel(f"გაცემის თარიღი: {visa['issue_date']}\nმოქმედების ვადა: {visa['expiration_date']}")
            
            layout.addWidget(id_status_label)
            layout.addWidget(country_type_label)
            layout.addWidget(dates_label)

            layout.setStretch(0, 1)
            layout.setStretch(1, 1)
            
            container = QtWidgets.QFrame()
            container.setLayout(layout)

            container.setStyleSheet("""
                QFrame {
                    background-color: rgba(240, 240, 240);
                    border-radius: 5px;
                }
            """)
            self.visa_content.addWidget(container)
    
    def update_fine__(self, data):
        for content in [self.id_content, self.car_fine_content]:
            for i in reversed(range(content.count())):
                widget = content.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()
        
        for fine in data:
            layout = QtWidgets.QHBoxLayout()
            layout.setContentsMargins(5, 10, 5, 10)
            layout.setSpacing(10)
            id_type_label = QtWidgets.QLabel(f"ჯარიმის ID: {fine['fine_id']}{f'\nმანქანის ID: {fine['car_id']}' if fine['car_id'] else ''}")
            amount_label = QtWidgets.QLabel(f"ღირებულება: {fine['amount']}")
            message_label = QtWidgets.QLabel(f"დამატებითი ინფ: {fine['message']}\nტიპი: {fine['type']}")
            message_label.setWordWrap(True)
            message_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                QtWidgets.QSizePolicy.Preferred)
            payment_btn = QtWidgets.QPushButton(f"{fine["status"]}")
            
            if payment_btn.text() == "გადახდილი":
                payment_btn.setEnabled(False)

            payment_btn.clicked.connect(lambda checked, btn=payment_btn, id=fine["fine_id"]: self.payment__(btn, id))

            layout.addWidget(id_type_label)
            layout.addWidget(amount_label)
            layout.addWidget(message_label, 2) 
            layout.addWidget(payment_btn)

            layout.setStretch(0, 1)
            layout.setStretch(1, 1)
            
            container = QtWidgets.QFrame()
            container.setLayout(layout)

            container.setStyleSheet("""
                QFrame {
                    background-color: rgba(240, 240, 240);
                    border-radius: 5px;
                }
            """)
            if fine["type"] == "საგზაო":
                self.car_fine_content.addWidget(container)
            else:
                self.id_content.addWidget(container)
    
    def data_fetch__(self):
        try:
            headers = {
                "Authorization": f"Bearer {AppState.token}"
            }

            user = requests.get("http://127.0.0.1:8000/data_fetch", headers=headers)
            fine = requests.get("http://127.0.0.1:8000/data_fetch/fine", headers=headers)
            borderstamp = requests.get("http://127.0.0.1:8000/data_fetch/borderstamp", headers=headers)
            visa = requests.get("http://127.0.0.1:8000/data_fetch/visa", headers=headers)
            car = requests.get("http://127.0.0.1:8000/data_fetch/car", headers=headers)
            
            res = {}

            if user.status_code == 200:
                res["user"] = user.json()
            else:
                QMessageBox.warning(self, "Failed", f"data fetch failed:\n{user.json()}")
                return
            
            for name, doc in {"fine": fine, "borderstamp": borderstamp, "visa": visa, "car": car}.items():
                if doc.status_code == 200:
                    res[f'{name}_list'] = doc.json()
                elif doc.status_code == 404:
                    res[f'{name}_list'] = None
                else:
                    QMessageBox.warning(self, "Failed", f"data fetch failed:\n{doc.json()}")
                    return
            return res
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

    def payment__(self, btn, fine_id):
        try:
            headers = {
                "Authorization": f"Bearer {AppState.token}"
            }

            response = requests.put(f"http://127.0.0.1:8000/data_fetch/update_fine_status/{fine_id}", headers=headers)
            if response.status_code == 200:
                btn.setText("გადახდილია")
                btn.setEnabled(False)
            else:
                QMessageBox.warning(self, "Failed", f"updating fine failed:\n{response.json()}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

class Border_guard(Border_guard_page, Universal_methods):
    def __init__(self, epass):
        super().__init__()
        self.border_guard_submit_btn.clicked.connect(self.submit__)
        self.border_guard_log_out_btn.clicked.connect(lambda: self.logout(epass))
        self.search_bar.returnPressed.connect(self.search)
        self.border_guard_search_btn.clicked.connect(self.search)

    def submit__(self):
        try:

            headers = {
                    "Authorization": f"Bearer {AppState.token}"
            }

            data = {
                "personal_id": self.border_guard_id_inp.text(),
                "location": self.border_guard_loc_inp.text(),
                "direction": self.border_group_dir_com.currentText()
            }

            response = requests.post("http://127.0.0.1:8000/borderstamp", headers=headers, json=data)

            if response.status_code == 201:
                print("borderstamp added successfully")
            else:
                QMessageBox.critical(self, "Failed", f"border stampt update failed:\n{response.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

class Police(Police_page, Universal_methods):
    def __init__(self, epass):
        super().__init__()
        self.police_submit_btn.clicked.connect(self.submit__)
        self.police_logout.clicked.connect(lambda: self.logout(epass))
        self.search_bar.returnPressed.connect(self.search)
        self.search_btn.clicked.connect(self.search)
        self.police_type_com.currentTextChanged.connect(self.toggle_car_inp__)
        self.police_car_inp.setVisible(False)
        self.police_submit_btn_1.clicked.connect(self.car_submit__)

    def toggle_car_inp__(self, text):
        is_sagzao = text == "საგზაო"
        
        self.police_car_inp.clear()
        self.police_car_inp.setVisible(is_sagzao)
    
    def car_submit__(self):
        try:
            headers = {
                    "Authorization": f"Bearer {AppState.token}"
            }

            data = {
                "car_id": self.police_car_inp_1.text(),
                "brand": self.police_brand_inp.text(),
                "model": self.police_model_inp.text(),
                "owner": self.police_id_inp_1.text()
            }

            response = requests.post("http://127.0.0.1:8000/car", headers=headers, json=data)

            if response.status_code == 201:
                print("car added successfully")
            else:
                QMessageBox.critical(self, "Failed", f"car update failed:\n{response.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

    def submit__(self):
        try:
            headers = {
                    "Authorization": f"Bearer {AppState.token}"
            }

            data = {
                "personal_id": self.police_id_inp.text(),
                "type": self.police_type_com.currentText(),
                "car_id": self.police_car_inp.text(),
                "message": self.police_msg_inp.text(),
                "amount": int(self.police_amount_inp.text()),
                "duration_days": int(self.police_dur_inp.text())
            }
            print(data)
            response = requests.post("http://127.0.0.1:8000/fine", headers=headers, json=data)

            if response.status_code == 201:
                print("fine added successfully")
            else:
                QMessageBox.critical(self, "Failed", f"fine update failed:\n{response.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

class Ambassador(Ambassador_page, Universal_methods):
    def __init__(self, epass):
        super().__init__()
        self.amb_submit_btn.clicked.connect(self.submit__)
        self.amb_log_out_btn.clicked.connect(lambda: self.logout(epass))
        self.search_bar.returnPressed.connect(self.search)
        self.amb_search_btn.clicked.connect(self.search)

    def submit__(self):
        try:
            headers = {
                    "Authorization": f"Bearer {AppState.token}"
            }

            data = {
                "personal_id": self.amb_id_inp.text(),
                "country": self.amb_country_inp.text(),
                "type": self.police_type_com.currentText(),
                "duration_years": int(self.amb_dur_inp.text())
            }

            response = requests.post("http://127.0.0.1:8000/visa", headers=headers, json=data)

            if response.status_code == 201:
                print("visa added successfully")
            else:
                QMessageBox.critical(self, "Failed", f"visa update failed:\n{response.json()["detail"]}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error connecting to server:\n{str(e)}")

if __name__ == "__main__":
    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()

    application = QApplication(sys.argv)
    window = Epass()
    window.show()
    sys.exit(application.exec_())