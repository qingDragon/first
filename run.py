import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from manual_test import Ui_Form
import RPi.GPIO as GPIO
import time
import threading

class mwindow(QWidget,Ui_Form):
    i = False

    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(11, GPIO.OUT)#控制z轴方向 竖直方向
        GPIO.setup(12, GPIO.OUT)#控制x轴方向 水平方向
        GPIO.setup(7, GPIO.OUT) #控制摄像头pwm输出
        # GPIO.setup(13, GPIO.OUT)#控制z轴方向
        GPIO.setup(13, GPIO.OUT) #控制摄像头方向
        GPIO.setup(15, GPIO.OUT)#控制z轴运动
        GPIO.setup(16, GPIO.OUT)#控制x轴运动
        # GPIO.setup(18, GPIO.OUT)#控制z轴运动
        #控制上下左右移动按钮与槽函数连接
        # self.pushButton.setCheckable(True)
        # self.pushButton.setAutoExclusive(True)

        self.pushButton.clicked.connect(self.up_run)
        self.pushButton_2.clicked.connect(self.left_run)

        self.pushButton_3.clicked.connect(self.right_run)
        self.pushButton_4.clicked.connect(self.down_run)
        self.pushButton_5.clicked.connect(self.test_run)
        self.pushButton_6.clicked.connect(self.stop)

        self.pushButton_7.clicked.connect(QApplication.quit)#退出按钮连接槽函数

    def test(self):
        while True:
            count =0

            mwindow.i = False

            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            while count < 1000:


                if mwindow.i:
                    break

                time.sleep(0.0001)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.0001)
                GPIO.output(15, GPIO.HIGH)
                print("finished up")

                time.sleep(0.0001)
                GPIO.output(16, GPIO.LOW)
                time.sleep(0.0001)
                GPIO.output(16, GPIO.HIGH)
                print("finished left!")
                # 摄像头移动
                time.sleep(0.0001)
                GPIO.output(7, GPIO.LOW)
                time.sleep(0.0001)
                GPIO.output(7, GPIO.HIGH)
                print("finished forward!")
                count += 1
            if mwindow.i:
                break
            count = 0
            GPIO.output(11, GPIO.LOW)#z轴方向
            GPIO.output(12, GPIO.LOW)#x轴方向
            GPIO.output(13, GPIO.LOW)#z轴方向
            while count < 1000:

                if mwindow.i:
                    break

                time.sleep(0.0001)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.0001)
                GPIO.output(15, GPIO.HIGH)
                print("finished down")
                time.sleep(0.0001)
                GPIO.output(16, GPIO.LOW)
                time.sleep(0.0001)
                GPIO.output(16, GPIO.HIGH)
                print("finished right")

                time.sleep(0.0001)
                GPIO.output(7, GPIO.LOW)
                time.sleep(0.0001)
                GPIO.output(7, GPIO.HIGH)
                print("finished behind!")
                count += 1
            if mwindow.i:
                break


    def test_run(self):
        t = threading.Thread(target=self.test)
        t.start()
    def stop(self):

        mwindow.i = True

    #向上运动(z轴)
    def up(self):

        mwindow.i = False
        GPIO.output(11, GPIO.HIGH)
        time.sleep(1)
        while True:
            if mwindow.i:
                break
            time.sleep(0.0008)
            GPIO.output(15, GPIO.HIGH)
            time.sleep(0.0008)
            GPIO.output(15, GPIO.LOW)
        print("finished up!")

    #向上运动线程
    def up_run(self):
        t = threading.Thread(target=self.up)
        t.start()


    #向下运动
    def down(self):

        mwindow.i = False
        GPIO.output(11, GPIO.LOW)
        time.sleep(1)# 控制上下方向
        while True:
            if mwindow.i:
                break
            time.sleep(0.0005)
            GPIO.output(15, GPIO.HIGH)
            time.sleep(0.0005)
            GPIO.output(15, GPIO.LOW)
        print("finished down!")
    #向下运动线程
    def down_run(self):

        t = threading.Thread(target=self.down)
        t.start()
    #向左运动(x轴)

    def left(self):
        mwindow.i = False
        count = 0
        GPIO.output(12, GPIO.HIGH) # 控制左右方向
        time.sleep(0.1)
        while count < 400:
            if mwindow.i:
                count =0
                break
            time.sleep(0.0006)
            GPIO.output(16, GPIO.LOW)
            time.sleep(0.0006)
            GPIO.output(16, GPIO.HIGH)
            count+=1
        count = 0
        while count < 400:
            if mwindow.i:
                count=0
                break
            time.sleep(0.0005)
            GPIO.output(16, GPIO.LOW)
            time.sleep(0.0005)
            GPIO.output(16, GPIO.HIGH)
            count+=1
        count = 0
        while count < 400:
            if mwindow.i:
                count = 0
                break
            time.sleep(0.0004)
            GPIO.output(16, GPIO.LOW)
            time.sleep(0.0004)
            GPIO.output(16, GPIO.HIGH)
            count+=1
        count = 0
        while count < 400:
            if mwindow.i:
                count = 0
                break
            time.sleep(0.0003)
            GPIO.output(16, GPIO.LOW)
            time.sleep(0.0003)
            GPIO.output(16, GPIO.HIGH)
            count+=1
        print("finished left!")

    def left_run(self):
        t = threading.Thread(target=self.left)
        t.start()
    #向右运动
    def right(self):
        mwindow.i = False

        GPIO.output(12, GPIO.LOW)# 控制左右方向
        time.sleep(0.1)
        while True:
            if mwindow.i:
                break
            time.sleep(0.0005)
            GPIO.output(16, GPIO.LOW)
            time.sleep(0.0005)
            GPIO.output(16, GPIO.HIGH)
        print("finished right!")


    def right_run(self):
        t = threading.Thread(target=self.right)
        t.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = mwindow()

    w.showFullScreen()
    sys.exit(app.exec())


#实时的坐标保存在哪？
#重置后，保存的坐标要清0
#复位，计算离零点距离，并调用三轴运动函数
#一个脉冲多少距离，计算运动的距离，更新x,y,z坐标
