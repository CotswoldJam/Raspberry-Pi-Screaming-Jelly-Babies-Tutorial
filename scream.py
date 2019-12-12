import time
import RPi.GPIO as GPIO
import os
print "Hello World!"

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.IN)

while True:
    if GPIO.input(3) == False:
        print "ow!"
        os.system("omxplayer scream-c.wav")
        time.sleep(1)
        
