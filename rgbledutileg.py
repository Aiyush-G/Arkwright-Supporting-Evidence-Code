from rgbledutil import rgbled
from random import randint
import time

led = rgbled(16,24,25)

try:
    while True:
        r = 0
        g = 255
        b = 0
        led.changeto(r,g,b,1)
        time.sleep(2)
        
except KeyboardInterrupt:
    led.off(0.1)
    led.cleanup()
