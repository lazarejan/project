from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtWidgets, QtGui

class AppState:
    token = None

class Welcome_page(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(750, 522)
        Welcome.setStyleSheet("\n"
            "QWidget {\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center;\n"
            "\n"
            "}\n"
            "    QFrame {\n"
            "        background-color: rgba(255, 255, 255, 30%);\n"
            "        border-radius: 15px;\n"
            "    }\n"
            "    QLineEdit {\n"
            "        border: 1px solid #ccc;\n"
            "        padding: 8px 12px;\n"
            "        border-radius: 15px;\n"
            "        background-color: rgba(255, 255, 255, 80%);\n"
            "    }\n"
            "  \n"
            "    \n"
            "    QLabel {\n"
            "        color: black;\n"
            "    }")
        self.welcome_grid = QtWidgets.QGridLayout(Welcome)
        self.welcome_grid.setObjectName("welcome_grid")
        self.welcome_container = QtWidgets.QFrame(Welcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_container.sizePolicy().hasHeightForWidth())
        self.welcome_container.setSizePolicy(sizePolicy)
        self.welcome_container.setMinimumSize(QtCore.QSize(400, 500))
        self.welcome_container.setMaximumSize(QtCore.QSize(400, 500))
        self.welcome_container.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.welcome_container.setObjectName("welcome_container")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.welcome_container)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.welcome_head = QtWidgets.QLabel(self.welcome_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_head.sizePolicy().hasHeightForWidth())
        self.welcome_head.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_head.setFont(font)
        self.welcome_head.setToolTip("")
        self.welcome_head.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_head.setObjectName("welcome_head")
        self.gridLayout_4.addWidget(self.welcome_head, 1, 0, 1, 1)
        self.welcome_btn_container = QtWidgets.QHBoxLayout()
        self.welcome_btn_container.setObjectName("welcome_btn_container")
        self.login_btn = QtWidgets.QPushButton(self.welcome_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.login_btn.setObjectName("login_btn")
        self.welcome_btn_container.addWidget(self.login_btn)
        self.register_btn = QtWidgets.QPushButton(self.welcome_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.register_btn.setObjectName("register_btn")
        self.welcome_btn_container.addWidget(self.register_btn)
        self.gridLayout_4.addLayout(self.welcome_btn_container, 3, 0, 1, 1)
        self.welcome_grid.addWidget(self.welcome_container, 0, 0, 1, 1)

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Form"))
        self.welcome_head.setText(_translate("Welcome", "Epass"))
        self.login_btn.setText(_translate("Welcome", "Login"))
        self.register_btn.setText(_translate("Welcome", "Register"))

class Login_page(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Loginpage):
        Loginpage.setObjectName("Loginpage")
        Loginpage.resize(874, 621)
        Loginpage.setStyleSheet("\n"
            "    QWidget {\n"
            "        background-repeat: no-repeat;\n"
            "        background-position: center;\n"
            "    }\n"
            "    QFrame {\n"
            "        background-color: rgba(255, 255, 255, 30%);\n"
            "        border-radius: 15px;\n"
            "    }\n"
            "    QLineEdit {\n"
            "        border: 1px solid #ccc;\n"
            "        padding: 8px 12px;\n"
            "        border-radius: 15px;\n"
            "        background-color: rgba(255, 255, 255, 80%);\n"
            "    }\n"
            "    QPushButton {\n"
            "      \n"
            " \n"
            "    }\n"
            "    QLabel {\n"
            "        color:black;\n"
            "    }\n"
            "   \n"
            "   ")
        self.login_grid = QtWidgets.QGridLayout(Loginpage)
        self.login_grid.setContentsMargins(-1, -1, 11, -1)
        self.login_grid.setObjectName("login_grid")
        self.loginFrame = QtWidgets.QFrame(Loginpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginFrame.sizePolicy().hasHeightForWidth())
        self.loginFrame.setSizePolicy(sizePolicy)
        self.loginFrame.setMinimumSize(QtCore.QSize(400, 320))
        self.loginFrame.setMaximumSize(QtCore.QSize(400, 320))
        self.loginFrame.setToolTipDuration(-1)
        self.loginFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setLineWidth(1)
        self.loginFrame.setObjectName("loginFrame")
        self.frameLayout = QtWidgets.QVBoxLayout(self.loginFrame)
        self.frameLayout.setObjectName("frameLayout")
        self.login_header = QtWidgets.QLabel(self.loginFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_header.setFont(font)
        self.login_header.setToolTip("")
        self.login_header.setAlignment(QtCore.Qt.AlignCenter)
        self.login_header.setObjectName("login_header")
        self.frameLayout.addWidget(self.login_header)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.frameLayout.addItem(spacerItem)
        self.username_inp = QtWidgets.QLineEdit(self.loginFrame)
        self.username_inp.setObjectName("username_inp")
        self.frameLayout.addWidget(self.username_inp)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_inp = QtWidgets.QLineEdit(self.loginFrame)
        self.password_inp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_inp.setObjectName("password_inp")
        self.horizontalLayout_2.addWidget(self.password_inp)
        self.echo_toggle_btn = QtWidgets.QPushButton(self.loginFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.echo_toggle_btn.sizePolicy().hasHeightForWidth())
        self.echo_toggle_btn.setSizePolicy(sizePolicy)
        self.echo_toggle_btn.setMinimumSize(QtCore.QSize(30, 0))
        self.echo_toggle_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.echo_toggle_btn.setObjectName("echo_toggle_btn")
        self.horizontalLayout_2.addWidget(self.echo_toggle_btn)
        self.frameLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frameLayout.addItem(spacerItem1)
        self.login_btn_container = QtWidgets.QHBoxLayout()
        self.login_btn_container.setObjectName("login_btn_container")
        self.back_btn = QtWidgets.QPushButton(self.loginFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMaximumSize(QtCore.QSize(150, 150))
        self.back_btn.setObjectName("back_btn")
        self.login_btn_container.addWidget(self.back_btn)
        self.login_btn = QtWidgets.QPushButton(self.loginFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.login_btn.setObjectName("login_btn")
        self.login_btn_container.addWidget(self.login_btn)
        self.frameLayout.addLayout(self.login_btn_container)
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.frameLayout.addItem(spacerItem2)
        self.login_grid.addWidget(self.loginFrame, 0, 0, 1, 1)

        self.retranslateUi(Loginpage)
        QtCore.QMetaObject.connectSlotsByName(Loginpage)

    def retranslateUi(self, Loginpage):
        _translate = QtCore.QCoreApplication.translate
        self.login_header.setText(_translate("Loginpage", "Login"))
        self.username_inp.setPlaceholderText(_translate("Loginpage", "Username"))
        self.password_inp.setPlaceholderText(_translate("Loginpage", "Password"))
        self.echo_toggle_btn.setText(_translate("Loginpage", "👁️"))
        self.back_btn.setText(_translate("Loginpage", "Back"))
        self.login_btn.setText(_translate("Loginpage", "Login"))

class Register_page(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Registerpage):
        Registerpage.setObjectName("Registerpage")
        Registerpage.resize(868, 619)
        Registerpage.setStyleSheet("\n"
            "    QWidget {\n"
            "        background-repeat: no-repeat;\n"
            "        background-position: center;\n"
            "    }\n"
            "    QFrame {\n"
            "        background-color: rgba(255, 255, 255, 30%);\n"
            "        border-radius: 15px;\n"
            "    }\n"
            "    QLineEdit {\n"
            "        border: 1px solid #ccc;\n"
            "        padding: 8px 12px;\n"
            "        border-radius: 15px;\n"
            "        background-color: rgba(255, 255, 255, 80%);\n"
            "    }\n"
            "    QPushButton {\n"
            "      \n"
            " \n"
            "    }\n"
            "    QLabel {\n"
            "        color:black;\n"
            "    }\n"
            "   ")
        self.register_grid = QtWidgets.QGridLayout(Registerpage)
        self.register_grid.setObjectName("register_grid")
        self.registerFrame = QtWidgets.QFrame(Registerpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerFrame.sizePolicy().hasHeightForWidth())
        self.registerFrame.setSizePolicy(sizePolicy)
        self.registerFrame.setMinimumSize(QtCore.QSize(360, 350))
        self.registerFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.registerFrame.setObjectName("registerFrame")
        self.frameLayout = QtWidgets.QVBoxLayout(self.registerFrame)
        self.frameLayout.setContentsMargins(50, -1, 50, -1)
        self.frameLayout.setObjectName("frameLayout")
        self.register_header = QtWidgets.QLabel(self.registerFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_header.setFont(font)
        self.register_header.setAlignment(QtCore.Qt.AlignCenter)
        self.register_header.setObjectName("register_header")
        self.frameLayout.addWidget(self.register_header)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frameLayout.addItem(spacerItem)
        self.personal_num_inp = QtWidgets.QLineEdit(self.registerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personal_num_inp.sizePolicy().hasHeightForWidth())
        self.personal_num_inp.setSizePolicy(sizePolicy)
        self.personal_num_inp.setMaximumSize(QtCore.QSize(250, 40))
        self.personal_num_inp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.personal_num_inp.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.personal_num_inp.setObjectName("personal_num_inp")
        self.frameLayout.addWidget(self.personal_num_inp)
        self.username_inp = QtWidgets.QLineEdit(self.registerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_inp.sizePolicy().hasHeightForWidth())
        self.username_inp.setSizePolicy(sizePolicy)
        self.username_inp.setMaximumSize(QtCore.QSize(250, 16777215))
        self.username_inp.setObjectName("username_inp")
        self.frameLayout.addWidget(self.username_inp)
        self.password_inp = QtWidgets.QLineEdit(self.registerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_inp.sizePolicy().hasHeightForWidth())
        self.password_inp.setSizePolicy(sizePolicy)
        self.password_inp.setMaximumSize(QtCore.QSize(250, 16777215))
        self.password_inp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_inp.setObjectName("password_inp")
        self.frameLayout.addWidget(self.password_inp)
        self.rpassword_inp = QtWidgets.QLineEdit(self.registerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpassword_inp.sizePolicy().hasHeightForWidth())
        self.rpassword_inp.setSizePolicy(sizePolicy)
        self.rpassword_inp.setMaximumSize(QtCore.QSize(250, 16777215))
        self.rpassword_inp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rpassword_inp.setObjectName("rpassword_inp")
        self.frameLayout.addWidget(self.rpassword_inp)
        self.register_btn_container = QtWidgets.QHBoxLayout()
        self.register_btn_container.setObjectName("register_btn_container")
        self.back_btn = QtWidgets.QPushButton(self.registerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMaximumSize(QtCore.QSize(150, 150))
        self.back_btn.setObjectName("back_btn")
        self.register_btn_container.addWidget(self.back_btn)
        self.register_btn = QtWidgets.QPushButton(self.registerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.register_btn.setObjectName("register_btn")
        self.register_btn_container.addWidget(self.register_btn)
        self.frameLayout.addLayout(self.register_btn_container)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frameLayout.addItem(spacerItem1)
        self.register_grid.addWidget(self.registerFrame, 1, 0, 1, 1)

        self.retranslateUi(Registerpage)
        QtCore.QMetaObject.connectSlotsByName(Registerpage)

    def retranslateUi(self, Registerpage):
        _translate = QtCore.QCoreApplication.translate
        self.register_header.setText(_translate("Registerpage", "Register"))
        self.personal_num_inp.setPlaceholderText(_translate("Registerpage", "Personal number"))
        self.username_inp.setPlaceholderText(_translate("Registerpage", "Username"))
        self.password_inp.setPlaceholderText(_translate("Registerpage", "Password"))
        self.rpassword_inp.setPlaceholderText(_translate("Registerpage", "Repeat password"))
        self.back_btn.setText(_translate("Registerpage", "Back"))
        self.register_btn.setText(_translate("Registerpage", "Register"))
