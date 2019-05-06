# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\MyProjects\Python\rep\editor_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(828, 700)
        Form.setMinimumSize(QtCore.QSize(576, 536))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.exitEditorBtn = QtWidgets.QPushButton(Form)
        self.exitEditorBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.exitEditorBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.exitEditorBtn.setStyleSheet("background-color: rgb(255, 57, 57);")
        self.exitEditorBtn.setObjectName("exitEditorBtn")
        self.horizontalLayout_4.addWidget(self.exitEditorBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.maxEditorBtn = QtWidgets.QPushButton(Form)
        self.maxEditorBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.maxEditorBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.maxEditorBtn.setObjectName("maxEditorBtn")
        self.horizontalLayout_4.addWidget(self.maxEditorBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.minEditorBtn = QtWidgets.QPushButton(Form)
        self.minEditorBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.minEditorBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.minEditorBtn.setStyleSheet("")
        self.minEditorBtn.setObjectName("minEditorBtn")
        self.horizontalLayout_4.addWidget(self.minEditorBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_4.setStretch(2, 3000)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.openFolderBtn = QtWidgets.QPushButton(Form)
        self.openFolderBtn.setMinimumSize(QtCore.QSize(30, 20))
        self.openFolderBtn.setMaximumSize(QtCore.QSize(30, 20))
        self.openFolderBtn.setObjectName("openFolderBtn")
        self.horizontalLayout_3.addWidget(self.openFolderBtn)
        self.shareBtn = QtWidgets.QPushButton(Form)
        self.shareBtn.setMinimumSize(QtCore.QSize(30, 20))
        self.shareBtn.setMaximumSize(QtCore.QSize(30, 20))
        self.shareBtn.setObjectName("shareBtn")
        self.horizontalLayout_3.addWidget(self.shareBtn)
        self.saveReportBtn = QtWidgets.QPushButton(Form)
        self.saveReportBtn.setMinimumSize(QtCore.QSize(23, 20))
        self.saveReportBtn.setMaximumSize(QtCore.QSize(50, 20))
        self.saveReportBtn.setObjectName("saveReportBtn")
        self.horizontalLayout_3.addWidget(self.saveReportBtn)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(141, 61))
        self.groupBox.setMaximumSize(QtCore.QSize(141, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reportNumberTb = QtWidgets.QLineEdit(self.groupBox)
        self.reportNumberTb.setMinimumSize(QtCore.QSize(30, 20))
        self.reportNumberTb.setMaximumSize(QtCore.QSize(30, 20))
        self.reportNumberTb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reportNumberTb.setAlignment(QtCore.Qt.AlignCenter)
        self.reportNumberTb.setObjectName("reportNumberTb")
        self.horizontalLayout.addWidget(self.reportNumberTb)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dateEdit.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(151, 61))
        self.groupBox_2.setMaximumSize(QtCore.QSize(151, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rubCountTb = QtWidgets.QLineEdit(self.groupBox_2)
        self.rubCountTb.setAlignment(QtCore.Qt.AlignCenter)
        self.rubCountTb.setObjectName("rubCountTb")
        self.horizontalLayout_2.addWidget(self.rubCountTb)
        self.kopCountTb = QtWidgets.QLineEdit(self.groupBox_2)
        self.kopCountTb.setMinimumSize(QtCore.QSize(30, 20))
        self.kopCountTb.setMaximumSize(QtCore.QSize(30, 20))
        self.kopCountTb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.kopCountTb.setObjectName("kopCountTb")
        self.horizontalLayout_2.addWidget(self.kopCountTb)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setMinimumSize(QtCore.QSize(181, 91))
        self.groupBox_4.setMaximumSize(QtCore.QSize(181, 91))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_4, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setMinimumSize(QtCore.QSize(551, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.addDocBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.addDocBtn.setObjectName("addDocBtn")
        self.gridLayout.addWidget(self.addDocBtn, 0, 4, 1, 1, QtCore.Qt.AlignRight)
        self.docNumTb = QtWidgets.QLineEdit(self.groupBox_3)
        self.docNumTb.setMinimumSize(QtCore.QSize(151, 20))
        self.docNumTb.setAlignment(QtCore.Qt.AlignCenter)
        self.docNumTb.setObjectName("docNumTb")
        self.gridLayout.addWidget(self.docNumTb, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.docSum = QtWidgets.QLineEdit(self.groupBox_3)
        self.docSum.setMinimumSize(QtCore.QSize(151, 20))
        self.docSum.setAlignment(QtCore.Qt.AlignCenter)
        self.docSum.setObjectName("docSum")
        self.gridLayout.addWidget(self.docSum, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.docNameTb = QtWidgets.QLineEdit(self.groupBox_3)
        self.docNameTb.setMinimumSize(QtCore.QSize(151, 20))
        self.docNameTb.setAlignment(QtCore.Qt.AlignCenter)
        self.docNameTb.setObjectName("docNameTb")
        self.gridLayout.addWidget(self.docNameTb, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.docDate = QtWidgets.QDateEdit(self.groupBox_3)
        self.docDate.setMinimumSize(QtCore.QSize(151, 20))
        self.docDate.setAlignment(QtCore.Qt.AlignCenter)
        self.docDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.docDate.setObjectName("docDate")
        self.gridLayout.addWidget(self.docDate, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.delDocBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.delDocBtn.setObjectName("delDocBtn")
        self.gridLayout.addWidget(self.delDocBtn, 0, 5, 1, 1)
        self.gridLayout.setColumnStretch(3, 2000)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setMinimumSize(QtCore.QSize(511, 301))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Отчет"))
        self.exitEditorBtn.setText(_translate("Form", "✖"))
        self.maxEditorBtn.setText(_translate("Form", "☐"))
        self.minEditorBtn.setText(_translate("Form", "_"))
        self.openFolderBtn.setText(_translate("Form", "📂"))
        self.shareBtn.setText(_translate("Form", "📤"))
        self.saveReportBtn.setText(_translate("Form", "💾"))
        self.groupBox.setTitle(_translate("Form", "Авансовый отчет"))
        self.reportNumberTb.setPlaceholderText(_translate("Form", "№"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Город"))
        self.groupBox_2.setTitle(_translate("Form", "Отчет в сумме"))
        self.rubCountTb.setPlaceholderText(_translate("Form", "руб."))
        self.kopCountTb.setPlaceholderText(_translate("Form", "коп."))
        self.label.setText(_translate("Form", "₽"))
        self.groupBox_4.setTitle(_translate("Form", "Подотчетное лицо"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "ФИО"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Должность"))
        self.groupBox_3.setTitle(_translate("Form", "Документы"))
        self.addDocBtn.setText(_translate("Form", "➕"))
        self.docNumTb.setPlaceholderText(_translate("Form", "Номер документа"))
        self.docSum.setPlaceholderText(_translate("Form", "Сумма"))
        self.docNameTb.setPlaceholderText(_translate("Form", "Название документа"))
        self.delDocBtn.setText(_translate("Form", "➖"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Документ"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Номер "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Сумма"))

