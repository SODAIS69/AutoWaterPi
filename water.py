import time as time
import RPi.GPIO as GPIO


def water():
    pin=16
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT) #water pump
    GPIO.output(pin, 0)
    time.sleep(1.7)
    GPIO.output(pin, 1)