import time as time
import RPi.GPIO as GPIO

def PumpWater():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT) #water pump
    GPIO.output(37, 0)
    time.sleep(5)
    GPIO.output(37, 1)