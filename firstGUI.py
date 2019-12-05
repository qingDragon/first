
from PyQt5 import  QtWidgets

import  sys
app = QtWidgets.QApplication(sys.argv)
first_window = QtWidgets.QWidget()
first_window.resize(400,300)
first_window.setWindowTitle("我的第一个pyqt程序")
first_window.show()
label = QtWidgets.QLabel('helloworld')
sys.exit(app.exec())