#Check moist of dust and water level in tray
import RPi.GPIO as GPIO
import water
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)         #Water read
GPIO.setup(3, GPIO.IN)         #Moist read

WaterThreshold=30678
MoistThreshold=30678

if water>Threshold:
    remind user
if moist<threshold:
    watering()