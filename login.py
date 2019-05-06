import os
import sys
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import editorForm
import editor_form
import login_form
import window_movement

class Login(QtWidgets.QDialog, login_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.backBtn.clicked.connect(self.close)
        self.loginBtn.clicked.connect(self.login_func)

    def login_func(self):
        pass

def main():
    signin_form = QtWidgets.QApplication(sys.argv)
    signin_form.setStyle('Fusion')
    login_win = Login()
    window_movement.setMoveWindow(login_win)
    login_win.show()
    login_win.exec_()