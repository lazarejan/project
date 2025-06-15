from PyQt5.QtWidgets import (QApplication, QSizePolicy, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, 
                             QLabel, QLineEdit, QFormLayout, QHBoxLayout, QMessageBox, QDialog, QGridLayout)
from PyQt5 import QtCore, QtWidgets
import requests
from authentication import AppState

class Welcome_page(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(863, 665)
        Welcome.setStyleSheet("")
        self.welcome_grid = QtWidgets.QGridLayout(Welcome)
        self.welcome_grid.setObjectName("welcome_grid")
        self.welcome_head = QtWidgets.QGridLayout()
        self.welcome_head.setObjectName("welcome_head")
        spacerItem = QtWidgets.QSpacerItem(20, 350, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.welcome_head.addItem(spacerItem, 1, 0, 1, 1)
        self.welcome_head_txt = QtWidgets.QLabel(Welcome)
        self.welcome_head_txt.setStyleSheet("font-size: 100px;\n"
"font-weight: bold;\n"
"color: #333333;")
        self.welcome_head_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_head_txt.setObjectName("welcome_head_txt")
        self.welcome_head.addWidget(self.welcome_head_txt, 0, 0, 1, 1)
        self.welcome_grid.addLayout(self.welcome_head, 0, 0, 1, 1)
        self.button_container = QtWidgets.QGridLayout()
        self.button_container.setObjectName("button_container")
        self.Login_btn = QtWidgets.QPushButton(Welcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login_btn.sizePolicy().hasHeightForWidth())
        self.Login_btn.setSizePolicy(sizePolicy)
        self.Login_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Login_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Login_btn.setMouseTracking(False)
        self.Login_btn.setTabletTracking(False)
        self.Login_btn.setAcceptDrops(False)
        self.Login_btn.setAutoFillBackground(False)
        self.Login_btn.setStyleSheet("font-size: 18px\n"
"")
        self.Login_btn.setAutoDefault(False)
        self.Login_btn.setDefault(False)
        self.Login_btn.setFlat(False)
        self.Login_btn.setObjectName("Login_btn")
        self.button_container.addWidget(self.Login_btn, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.button_container.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.button_container.addItem(spacerItem2, 1, 0, 1, 1)
        self.Register_btn = QtWidgets.QPushButton(Welcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Register_btn.sizePolicy().hasHeightForWidth())
        self.Register_btn.setSizePolicy(sizePolicy)
        self.Register_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Register_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Register_btn.setStyleSheet("font-size: 18px")
        self.Register_btn.setObjectName("Register_btn")
        self.button_container.addWidget(self.Register_btn, 0, 0, 1, 1)
        self.welcome_grid.addLayout(self.button_container, 2, 0, 1, 1)

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Form"))
        self.welcome_head_txt.setText(_translate("Welcome", "Epass"))
        self.Login_btn.setText(_translate("Welcome", "Log in"))
        self.Register_btn.setToolTip(_translate("Welcome", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Register_btn.setText(_translate("Welcome", "Register"))

