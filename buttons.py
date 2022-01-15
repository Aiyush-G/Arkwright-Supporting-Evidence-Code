import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

p1 = 17
p2 = 27
p3 = 22

def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.p)  # Use physical pin numbering

GPIO.setup(p1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(p2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(p3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(p1,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(p2,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(p3,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up