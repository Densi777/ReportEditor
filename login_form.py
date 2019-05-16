# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(185, 172)
        Form.setMinimumSize(QtCore.QSize(185, 172))
        Form.setMaximumSize(QtCore.QSize(185, 172))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
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
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginTb = QtWidgets.QLineEdit(Form)
        self.loginTb.setAlignment(QtCore.Qt.AlignCenter)
        self.loginTb.setObjectName("loginTb")
        self.verticalLayout.addWidget(self.loginTb)
        self.passwordTb = QtWidgets.QLineEdit(Form)
        self.passwordTb.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passwordTb.setText("")
        self.passwordTb.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordTb.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordTb.setObjectName("passwordTb")
        self.verticalLayout.addWidget(self.passwordTb)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setEnabled(False)
        self.loginBtn.setMinimumSize(QtCore.QSize(60, 20))
        self.loginBtn.setMaximumSize(QtCore.QSize(60, 20))
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.backBtn = QtWidgets.QPushButton(Form)
        self.backBtn.setMinimumSize(QtCore.QSize(40, 20))
        self.backBtn.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.loginTb.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.passwordTb.setPlaceholderText(_translate("Form", "Пароль"))
        self.loginBtn.setText(_translate("Form", "Войти"))
        self.backBtn.setText(_translate("Form", "↩️"))

