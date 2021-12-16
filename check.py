#Check moist of dust and water level in tray
import time
import RPi.GPIO as GPIO
from water import water
from moisture import GetMoistureAndSave
from genChart import GenerateMoistureChart 
from waterlevel import GetWaterLevel
from pump import PumpWater
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)         #Water read
GPIO.setup(3, GPIO.IN)         #Moist read
WaterLevel=GetWaterLevel()
WaterThreshold=510
MoistThreshold=70
Moisture=GetMoistureAndSave()
GenerateMoistureChart()

if Moisture<MoistThreshold:
    water()

time.sleep(20)
if WaterLevel>WaterThreshold:
  PumpWater()
 #   remind user
#if Moisture<threshold:
#  water()
