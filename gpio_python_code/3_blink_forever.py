from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# setup our output pins
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
while True:
         print ("lights on")
         GPIO.output(17,GPIO.HIGH)
         GPIO.output(27,GPIO.HIGH)
         
         sleep(1)

         print ("lights off")
         GPIO.output(17,GPIO.LOW)
         GPIO.output(27,GPIO.LOW)
         sleep(1)


