#!/usr/bin/python
import RPi.GPIO as GPIO   
GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme.  
 
   
GPIO.setup(16, GPIO.OUT)# set GPIO 17 as output for white led  
GPIO.setup(24, GPIO.OUT)# set GPIO 27 as output for red led  
GPIO.setup(25, GPIO.OUT)# set GPIO 22 as output for red led
   
hz = input('Please define the frequency in Herz(recommended:75): ')
reddc = input('Please define the red LED Duty Cycle: ')
greendc = input('Please define the green LED Duty Cycle: ')
bluedc = input('Please define the blue LED Duty Cycle: ')
 
red = GPIO.PWM(int(16), int(hz))    # create object red for PWM on port 17  
green = GPIO.PWM(int(24), int(hz))      # create object green for PWM on port 27   
blue = GPIO.PWM(int(25), int(hz))      # create object blue for PWM on port 22 
 
try:   
    while True:
        red.start((float(reddc)/2.55))   #start red led
        green.start((float(greendc)/2.55)) #start green led
        blue.start((float(bluedc)/2.55))  #start blue led
  
except KeyboardInterrupt:
        red.stop()   #stop red led
        green.stop() #stop green led
        blue.stop()  #stop blue led
   
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit 
