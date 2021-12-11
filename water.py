import time as time
import RPi.GPIO as GPIO


def water():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT) #water pump
    GPIO.output(16, 0)
    time.sleep(0.6)
    GPIO.output(16, 1)