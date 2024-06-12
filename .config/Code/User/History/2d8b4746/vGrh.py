import RPi.GPIO as GPIO # IMPORTANT: remember to change the gpio pin (18) also it needs to be programmed in Thonny Python IDE
import time #used in raspberry pi model 4

GPIO.setwarnings(False) #NOTE: raspberry pi could be updated, and you might need to change your code
GPIO.setmode(GPIO.BCM) 
GPIO.setup(15, GPIO.OUT)


while True:
      GPIO.output(15, True) 
      time.sleep(1) 
      GPIO.output(15, False) 
      time.sleep(1) 
