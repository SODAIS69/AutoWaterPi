#Check moist of dust and water level in tray
import RPi.GPIO as GPIO
from water import water
from moisture import GetMoistureAndSave
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)         #Water read
GPIO.setup(3, GPIO.IN)         #Moist read

WaterThreshold=30
MoistThreshold=30
Moisture=GetMoistureAndSave()
#print(Moisture)

#if water>Threshold:
 #   remind user
#if Moisture<threshold:
#  water()