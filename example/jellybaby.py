import time
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)
print "Hello World"
while True:
    if GPIO.input(3) == False:
        os.system('omxplayer scream-c.wav')
        time.sleep(1)
