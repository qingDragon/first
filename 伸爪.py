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

# 伸机械爪
GPIO.output(7,GPIO.HIGH)
time.sleep(1)
GPIO.output(7,GPIO.LOW)