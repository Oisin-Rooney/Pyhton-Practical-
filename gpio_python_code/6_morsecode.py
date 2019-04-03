import os
from time import sleep
import RPi.GPIO as GPIO

loop_count = 0

def morsecode():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setwarnings(False)

    GPIO.output(22,GPIO.HIGH)
    sleep(.1)
    GPIO.output(22,GPIO.LOW)
    sleep(.1)
    os.system('clear') # clear the screens text
    print ("Morse Code")
    GPIO.cleanup()

loop_count = int (input("How many times would you like SOS to loop?:"))
while loop_count > 0:
    if loop_count == 0:
        exit
    else:
        loop_count = loop_count-1    
        morsecode()