import sys
import serial
import RPi.GPIO as GPIO
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.palette1 = QtGui.QPalette()
        self.palette1.setColor(self.palette1.Background, QtGui.QColor("#02534a"))
        self.setPalette(self.palette1)
        self.btn0 = QPushButton("退出", self)
        #三个按钮控制串口输出
        self.btn1 = QPushButton("button1", self)
        self.btn2 = QPushButton("button2", self)
        self.btn3 = QPushButton("button3", self)
        #三个按钮控制gpio
        self.btn4 = QPushButton("正转", self)
        self.btn5 = QPushButton("反转", self)
        self.btn6 = QPushButton("停止", self)

        self.btn0.resize(100,30)


        self.btn1.resize(150,75)
        self.btn1.move(175,75)
        self.btn2.resize(150, 75)
        self.btn2.move(175, 200)
        self.btn3.resize(150, 75)
        self.btn3.move(175, 325)

        self.btn4.resize(150, 75)
        self.btn4.move(475, 75)
        self.btn5.resize(150, 75)
        self.btn5.move(475, 200)
        self.btn6.resize(150, 75)
        self.btn6.move(475, 325)





        self.btn0.clicked.connect(QApplication.quit)

        #控制串口输出的按钮连接槽函数
        # self.btn1.clicked.connect(lambda: self.sendMsg1(self.btn1.text()))
        self.btn1.clicked.connect(self.sendMsg1)
        self.btn2.clicked.connect(lambda: self.sendMsg1(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.sendMsg1(self.btn3.text()))

        self.btn4.clicked.connect(self.control_GPIO)
        self.btn5.clicked.connect(self.control_GPIO2)
        self.btn6.clicked.connect(self.stop_GPIO)

        #垂直布局-控制串口输出按钮
        # self.v1_layout = QVBoxLayout()
        # self.v1_layout.addWidget(self.btn1)
        # self.v1_layout.addWidget(self.btn2)
        # self.v1_layout.addWidget(self.btn3)
        #
        #
        # #垂直布局-控制gpio输出按钮
        # self.v2_layout = QVBoxLayout()
        # self.v2_layout.addWidget(self.btn4)
        # self.v2_layout.addWidget(self.btn5)
        # self.v2_layout.addWidget(self.btn6)
        #
        # self.h_layout = QHBoxLayout()
        # self.h_layout.addLayout(self.v1_layout)
        # self.h_layout.addLayout(self.v2_layout)

    # def sendMsg1(self, btn_name):
    #     ser = serial.Serial('/dev/ttyAMA0', 115200, parity=serial.PARITY_NONE)
    #     if ser.isOpen == False:
    #         ser.open()
    #     if btn_name== "button1":
    #         ser.write(b"")
    #     elif btn_name == "button2":
    #         ser.write(b"i am button2")
    #     elif btn_name == "button3":
    #         ser.write(b'i am button3')
    #     ser.close()
    #串口通信
    def sendMsg1(self):
        ser = serial.Serial('/dev/ttyAMA0', 9600, parity=serial.PARITY_NONE)
        if ser.isOpen == False:
            ser.open()
        ser.write(b'read')
        try:
            while 1:
                size = ser.inWaiting()
                if size != 0:
                    response = ser.read(size)
                    print(response)
                    ser.flushInput()

        except KeyboardInterrupt:
            ser.close()
    #反转
    def control_GPIO2(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.output(32,GPIO.LOW)
        GPIO.output(31, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(32, GPIO.HIGH)
    #停止
    def stop_GPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(32, GPIO.OUT)
        GPIO.output(32, GPIO.LOW)
    #正转
    def control_GPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(31, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(32, GPIO.HIGH)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.showFullScreen()
    sys.exit(app.exec())

