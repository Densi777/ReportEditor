import os
import sys
import postgresql
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import login_form
import start
import postgresql

import window_movement

class Login(QtWidgets.QDialog, login_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.backBtn.clicked.connect(self.close)
        self.loginBtn.clicked.connect(self.login_func)
        self.loginTb.textChanged.connect(self.on_text_changed)
        self.passwordTb.textChanged.connect(self.on_text_changed)

    def login_func(self):
        pass

    @QtCore.pyqtSlot()
    def on_text_changed(self):
        self.loginBtn.setEnabled(bool(self.loginTb.text()) and bool(self.passwordTb.text()))

def main():
    signin_form = QtWidgets.QApplication(sys.argv)
    signin_form.setStyle('Fusion')
    login_win = Login()
    window_movement.setMoveWindow(login_win)
    login_win.show()
    login_win.exec_()