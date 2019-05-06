import os
import sys
from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import start_form
import editorForm
import login
import window_movement

class ReportsApp(QtWidgets.QMainWindow, start_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.newBtn.clicked.connect(self.report)
        self.openBtn.clicked.connect(self.browse_folder)
        self.exitBtn.clicked.connect(self.exit_program)
        self.minBtn.clicked.connect(self.showMinimized)
        self.signInBtn.clicked.connect(self.login_show)
        self.tableWidget.itemDoubleClicked.connect(self.open_report)

    def browse_folder(self):
        self.tableWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку')

        if directory:
            for file_name in os.listdir(directory):
                self.tableWidget.addItem(file_name)

    def report(self):
        self.new_report = editorForm.ReportEditor()
        self.new_report.show()

    def login_show(self):
        self.sign_in = login.Login()
        self.sign_in.show()

    def open_report(self):
        pass

    def exit_program(self):
        QApplication.quit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ReportsApp()
    window_movement.setMoveWindow(window)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()