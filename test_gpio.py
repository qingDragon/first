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

#从中位移动至第一块表位置
def mid2first():
    count = 0
    GPIO.output(22, GPIO.LOW)  # 方向为正   HIGH往退料平台
    while count < 2500:
        time.sleep(0.0003)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(18, GPIO.LOW)
        count += 1
#打表函数
def dabiao():
    count = 0
    GPIO.output(16, GPIO.HIGH)  # 方向为正    LOW抬升，HIGH下降
    while count < 2000: #实际需要2500，测试用
        time.sleep(0.003)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.003)
        GPIO.output(12, GPIO.LOW)
        count += 1
    time.sleep(0.1)
    # 往上抬升
    count = 0
    GPIO.output(16, GPIO.LOW)  # 方向为正    LOW抬升，HIGH下降
    while count < 2000:
        time.sleep(0.0003)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(12, GPIO.LOW)
        count += 1
#进至下一块表函数
def nextbiao():
    count = 0
    GPIO.output(13, GPIO.LOW)  # 方向为正 ,LOW方向往里,HIGH方向往外
    while count < 13500:
        time.sleep(0.0003)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(11, GPIO.LOW)
        count += 1
#横向进至第二列
def next_to_2():
    count = 0
    GPIO.output(22, GPIO.HIGH)  # 方向为正   HIGH往退料平台
    while count < 10000:
        time.sleep(0.0003)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(18, GPIO.LOW)
        count += 1

#回至下一块表函数
def backbiao():
    count = 0
    GPIO.output(13, GPIO.HIGH)  # 方向为正 ,LOW方向往里,HIGH方向往外
    while count < 13500:
        time.sleep(0.0003)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(11, GPIO.LOW)
        count += 1
#处理完一箱回到中位
def back_2_mid():
    count = 0
    GPIO.output(22, GPIO.LOW)  # 方向为正   HIGH往退料平台
    while count < 17500:
        time.sleep(0.0003)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(18, GPIO.LOW)
        count += 1
#处理完一箱表x回位
def x_back():
    count = 0
    GPIO.output(13, GPIO.HIGH)  # 方向为正 ,LOW方向往里,HIGH方向往外
    while count < 40500:
        time.sleep(0.0003)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(11, GPIO.LOW)
        count += 1

def put_out():
    # 伸机械爪
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
def pull_back():
    # 机械爪缩回
    GPIO.output(15, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(15, GPIO.LOW)

#完整处理一箱循环过程
def  do_case():

    # 移动至第一列并完成该列打表
    mid2first()
    dabiao() #1
    nextbiao() #X轴往里13500到下一块表
    dabiao() #2
    nextbiao()
    dabiao() #3
    nextbiao()
    dabiao() #4

    # 移动至第二列并完成该列打表
    next_to_2()
    dabiao() #5
    backbiao()
    dabiao() #6
    backbiao()
    dabiao() #7
    backbiao()
    dabiao() #8

    # 移动至第三列并完成该列打表
    next_to_2()
    dabiao()  #9
    nextbiao()
    dabiao()  #10
    nextbiao()
    dabiao()  #11
    nextbiao()
    dabiao()  #12
    back_2_mid()
    x_back()

def up_3000():
    # 抬升整箱表3000
    count = 0
    GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
    while count < 3000:
        time.sleep(0.0003)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(12, GPIO.LOW)
        count += 1
def move2out():
 # 往退料平台平移44800
    count = 0
    GPIO.output(22, GPIO.HIGH)#方向为正   HIGH往退料平台
    while count < 44800:
        time.sleep(0.0003)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(18, GPIO.LOW)
        count += 1




#STEP1:从初始位置下降至第一箱表中位
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 9000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1
#STEP2:完成第一箱表处理并回到中位
do_case()
#STEP3：伸爪
put_out()
#STEP4: 抬升3000
up_3000()
#STEP5：移动至退料平台44800
move2out()
#STEP6:下降29200
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 29200:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1
#STEP7:缩爪
pull_back()
#STEP8:空载上升24000
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 24000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1
#STEP9:空载返回进料平台
count = 0
GPIO.output(22, GPIO.LOW)#方向为正   HIGH往退料平台
while count < 44800:
    time.sleep(0.0003)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(18, GPIO.LOW)
    count += 1

#STEP10:空载下降6500
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 6500:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1
#STEP11：第二箱表处理
do_case()
#STEP12:伸爪
put_out()
#STEP13: 抬升3000
up_3000()
#STEP14：移动至退料平台44800
move2out()

#STEP15:下降12000
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 12000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP16:缩爪
pull_back()

#STEP17:空载上升6000
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 6000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP18:空载返回进料平台
count = 0
GPIO.output(22, GPIO.LOW)#方向为正   HIGH往退料平台
while count < 44800:
    time.sleep(0.0003)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(18, GPIO.LOW)
    count += 1

#STEP19:空载下降6000
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 6000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1
#STEP20:第三箱表
do_case()

#STEP21:伸爪
put_out()

#STEP22:抬第三箱表上升12000
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 12000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP23：移动至退料平台44800
move2out()

#STEP24:第三箱表下降4000
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 4000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP25:缩爪
pull_back()

#STEP26：空载up6000
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 6000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP27:空载返回进料平台
count = 0
GPIO.output(22, GPIO.LOW)#方向为正   HIGH往退料平台
while count < 44800:
    time.sleep(0.0003)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(18, GPIO.LOW)
    count += 1

#STEP28:空载下降22000
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 22000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP29：第四箱
do_case()


#STEP30:伸爪
put_out()

#STEP31:抬第四箱表上升29000
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 29000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP32：移动至退料平台44800
move2out()

#STEP33:第四箱表下降4000
count = 0
GPIO.output(16, GPIO.HIGH)#方向为正    LOW抬升，HIGH下降
while count < 4000:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1

#STEP34:缩爪
pull_back()
#STEP35:空载上升9700
count = 0
GPIO.output(16, GPIO.LOW)#方向为正    LOW抬升，HIGH下降
while count < 9700:
    time.sleep(0.0003)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(12, GPIO.LOW)
    count += 1


#STEP36:空载返回进料平台
count = 0
GPIO.output(22, GPIO.LOW)#方向为正   HIGH往退料平台
while count < 44800:
    time.sleep(0.0003)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.0003)
    GPIO.output(18, GPIO.LOW)
    count += 1





