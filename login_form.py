# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\MyProjects\Python\rep\login_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(238, 194)
        Form.setMinimumSize(QtCore.QSize(238, 194))
        Form.setMaximumSize(QtCore.QSize(238, 194))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.backBtn = QtWidgets.QPushButton(Form)
        self.backBtn.setMinimumSize(QtCore.QSize(40, 20))
        self.backBtn.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginTb = QtWidgets.QLineEdit(Form)
        self.loginTb.setAlignment(QtCore.Qt.AlignCenter)
        self.loginTb.setObjectName("loginTb")
        self.verticalLayout.addWidget(self.loginTb)
        self.passwordTb = QtWidgets.QLineEdit(Form)
        self.passwordTb.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordTb.setObjectName("passwordTb")
        self.verticalLayout.addWidget(self.passwordTb)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setMinimumSize(QtCore.QSize(60, 20))
        self.loginBtn.setMaximumSize(QtCore.QSize(60, 20))
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout_2.addWidget(self.loginBtn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.backBtn.setText(_translate("Form", "↩️"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.loginTb.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.passwordTb.setPlaceholderText(_translate("Form", "Пароль"))
        self.loginBtn.setText(_translate("Form", "Войти"))

