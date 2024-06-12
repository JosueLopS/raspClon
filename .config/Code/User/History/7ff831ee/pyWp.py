#import necessary libraries
import time
from RPi.GPIO import *

#Set up GPIO mode
setmode(BCM)

#define the GPIO pin connected to the LED
led_pin = 17 #Example pin, change it to match to your setup

try:
    #set the LED pin as an output
    setup(led_pin. OUT)

    #Turn on the LED
    output(led_pin, HIGH)
    print("LED is ON")

    #Wait for 3 seconds
    time.sleep(3)
    
    #Turn off the LED
    output(led_pin, LOW)
    print("LED is OFF")

except KeyboardInterrupt:
    #if CTRL+C is pressed, clean up GPIO
    cleanup()