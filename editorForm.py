import os
import sys
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import editor_form
import login
import window_movement

class ReportEditor(QtWidgets.QDialog, editor_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.exitEditorBtn.clicked.connect(self.close)
        self.maxEditorBtn.clicked.connect(self.max_window)
        self.minEditorBtn.clicked.connect(self.showMinimized)
        self.addDocBtn.clicked.connect(self.add_doc)
        self.delDocBtn.clicked.connect(self.del_doc)

    def add_doc(self):
        temp_doc_name = self.docNameTb.text()
        temp_doc_num = self.docNumTb.text()
        temp_doc_date = self.docDate.text()
        temp_doc_sum = self.docSum.text()
        
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        
        self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(temp_doc_name))
        self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(temp_doc_num))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(temp_doc_date))
        self.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem(temp_doc_sum))

    def del_doc(self):
        row = self.tableWidget.currentRow()
        self.tableWidget.removeRow(row)

    def max_window(self):
        if not(self.isMaximized()):
            self.showMaximized()
        else:
            self.showNormal()

def main():
    editor_form = QtWidgets.QApplication(sys.argv)
    editor_form.setStyle('Fusion')
    editor_form_window = ReportEditor()
    editor_form_window.show()
    editor_form.exec_()