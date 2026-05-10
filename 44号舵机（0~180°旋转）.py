'''
这段代码可以实现舵机44号的正反180°旋转
'''

import RPi.GPIO as GPIO
import time
import atexit

atexit.register(GPIO.cleanup)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT, initial=False)

p = GPIO.PWM(23, 50)  # 50Hz
p.start(0)
time.sleep(2)

def move_to(angle):
    if angle < 0:
        angle = 0
    #if angle > 180:
    #    angle = 180

    print(angle)
    p.ChangeDutyCycle(3 + 9 * angle / 180)
    time.sleep(0.02)
    p.ChangeDutyCycle(0)
    time.sleep(1)

# 在这里指定角度
move_to(0)
time.sleep(1)
#move_to(10)
time.sleep(1)
move_to(205)
time.sleep(1)
p.stop()
GPIO.cleanup()
