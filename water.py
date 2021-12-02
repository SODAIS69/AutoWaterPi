import time as time
def watering():
    GPIO.setup(38888, GPIO.OUT) #water pump
    GPIO.output(38888, 1)
    time.sleep(2)
    GPIO.output(38888, 0)