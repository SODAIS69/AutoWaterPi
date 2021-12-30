import time as time
import RPi.GPIO as GPIO

def PumpWater():
    pin=37
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT) #water pump
    GPIO.output(pin, 0)
    time.sleep(5)
    GPIO.output(pin, 1)