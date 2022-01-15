import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering

p1 = 21


def callback():
    print("toggled")

GPIO.setup(p1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: 
    GPIO.dd_event_detect(p1,GPIO.RISING,callback=callback)