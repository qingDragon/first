import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from myUI import *
class MyWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.showFullScreen()
    sys.exit(app.exec())