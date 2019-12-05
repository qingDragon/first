
import RPi.GPIO as GPIO
import time
count = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
while count < 12000:
    time.sleep(0.0005)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(7, GPIO.LOW)
    count += 1