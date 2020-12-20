
import RPi.GPIO as GPIO
import time
count = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



GPIO.setup(12, GPIO.OUT)#Z轴pwm输出
GPIO.setup(16, GPIO.OUT)#Z轴方向
GPIO.setup(18, GPIO.OUT)#Y轴pwm输出
GPIO.setup(22, GPIO.OUT)#Y轴方向
GPIO.setup(7, GPIO.OUT)#机械爪伸
GPIO.setup(15, GPIO.OUT)#机械爪缩
GPIO.setup(11, GPIO.OUT)#X轴pwm
GPIO.setup(13, GPIO.OUT)#X轴方向


#Y轴往进料平台移动到第一块表位置，移动2000
count = 0
GPIO.output(22, GPIO.LOW)#方向为正   HIGH往退料平台
while count < 2000:
    time.sleep(0.0003)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(18, GPIO.LOW)
    count += 1

#Z轴向下钻第一块表，钻头下降3000
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 3000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1

#打完第一块表Z轴抬升
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 3000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1

#X轴向里运动至第二块表，11000个脉冲
count = 0
GPIO.output(13, GPIO.LOW)#方向为正 ,LOW方向往里,HIGH方向往外
while count < 11000:
    time.sleep(0.0005)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(11, GPIO.LOW)
    count += 1

#Z轴向下钻第二块表
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 3000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1

#打完第二块表Z轴抬升
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 3000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1

#Y轴向退料平台移动至起始位
count = 0
GPIO.output(22, GPIO.HIGH)#方向为正   HIGH往退料平台
while count < 2000:
    time.sleep(0.0005)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(18, GPIO.LOW)
    count += 1



# 伸机械爪
GPIO.output(7,GPIO.HIGH)
time.sleep(1)
GPIO.output(7,GPIO.LOW)
#
#往上抬升
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 20000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1

#
# # 往退料平台平移
count = 0
GPIO.output(22, GPIO.HIGH)#方向为正   HIGH往退料平台
while count < 44800:
    time.sleep(0.0005)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(18, GPIO.LOW)
    count += 1
#
# #
# 下降
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 20000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1
# # #
#
#机械爪缩回

GPIO.output(15,GPIO.HIGH)
time.sleep(1)
GPIO.output(15,GPIO.LOW)

#往上抬升
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 20000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1

# # 往进料平台平移
count = 0
GPIO.output(22, GPIO.LOW)#方向为正   HIGH往退料平台
while count < 44800:
    time.sleep(0.0003)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(18, GPIO.LOW)
    count += 1
#下降到起始位
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 20000:
    time.sleep(0.0005)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(12, GPIO.LOW)
    count += 1

count = 0
GPIO.output(13, GPIO.HIGH)#方向为正 ,LOW方向往里,HIGH方向往外
while count < 11000:
    time.sleep(0.0005)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(11, GPIO.LOW)
    count += 1


#X测试
# count = 0
# GPIO.output(13, GPIO.LOW)#方向为正 ,LOW方向往里,HIGH方向往外
# while count < 3000:
#     time.sleep(0.0005)
#     GPIO.output(11, GPIO.HIGH)
#     time.sleep(0.0005)
#     GPIO.output(11, GPIO.LOW)
#     count += 1
#
# count = 0
# GPIO.output(13, GPIO.HIGH)#方向为正 ,LOW方向往里,HIGH方向往外
# while count < 3000:
#     time.sleep(0.0005)
#     GPIO.output(11, GPIO.HIGH)
#     time.sleep(0.0005)
#     GPIO.output(11, GPIO.LOW)
#     count += 1