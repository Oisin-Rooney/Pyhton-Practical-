#!/usr/bin/python
import RPi.GPIO as GPIO # import a library
from time import sleep 
GPIO.setmode(GPIO.BCM) # set the pin numbering system to BCM
GPIO.setup(17,GPIO.OUT) # set GPIO17 as an OUTPUT
print ("beep") # print to the screen so we know what’s going on
GPIO.output(17,GPIO.HIGH) # set GPIO17 low, 3v3 will now be
# de-active on that pin
sleep(3)
GPIO.output(17,GPIO.LOW)
