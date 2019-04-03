import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
loop = 0
while (loop < 5000000):
 print ("LED on")
 GPIO.output(18,GPIO.HIGH)
 time.sleep(0.001)
 print ("LED off")
 GPIO.output(18,GPIO.LOW)
 time.sleep(0.001)
 loop = loop + 1
print ("Finished")
