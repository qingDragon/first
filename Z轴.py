
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


#打表速度
# #下降
# count = 0
# GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
# while count < 200:
#     time.sleep(0.0003)
#     GPIO.output(12, GPIO.HIGH)
#     time.sleep(0.0003)
#     GPIO.output(12, GPIO.LOW)
#     count += 1
# #
# time.sleep(0.1)

# 往上抬升
# count = 0
# GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
# while count < 5000:
#     time.sleep(0.0003)
#     GPIO.output(12, GPIO.HIGH)
#     time.sleep(0.0003)
#     GPIO.output(12, GPIO.LOW)
#     count += 1

#下降
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 300:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1