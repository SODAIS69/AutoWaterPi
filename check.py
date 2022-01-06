#Check moist of dust and water level in tray
import time
import RPi.GPIO as GPIO
from water import water
from moisture import GetMoistureAndSave
from genChart import GenerateMoistureChart 
from waterlevel import GetWaterLevel
from pump import PumpWater
from logger import log
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)         #Water read
GPIO.setup(3, GPIO.IN)         #Moist read
WaterLevel=GetWaterLevel()
WaterThreshold=510
MoistThreshold=50
Moisture=GetMoistureAndSave()
GenerateMoistureChart()
log(f"waterLV:{WaterLevel}")
if Moisture<MoistThreshold and WaterLevel<600:
    log("waterd")
    # water()

time.sleep(20)
if WaterLevel>WaterThreshold:
    log("pumped")
    PumpWater()

 #   remind user
#if Moisture<threshold:
#  water()
