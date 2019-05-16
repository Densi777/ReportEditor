import os
import sys
import postgresql
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import register_form
import start
import window_movement

class Register(QtWidgets.QDialog, register_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.signUpBtn.clicked.connect(self.sign_up)
        self.cancelBtn.clicked.connect(self.close)
        

    def sign_up(self):
        self.new_user = start.ReportsApp()
        new_user.create_user_query(self.surnameTb.text(), self.nameTb.text(), self.patronymicTb.text(), self.regLoginTb.text(), self.regPasswordTb.text())
        ok_button = QMessageBox.about(self, 'Готово!', 'Пользователь %s успешно создан' % (self.regLoginTb.text()))
        self.close()
        if ok_button == QMessageBox.Ok:
            QMessageBox.close()


def main():
    signup_form = QtWidgets.QApplication(sys.argv)
    signup_form.setStyle('Fusion')
    register_win = Register()
    window_movement.setMoveWindow(register_win)
    register_win.show()
    register_win.exec_()