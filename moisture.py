# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp  # To scale values
#from time import sleep  # To add delay
import time
import os


# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0) 


# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def MoistureDetect():
  output = analogInput(0) # Reading from CH0
  output = interp(output, [0, 1023], [0, 100])
  output = int(output)
  return output,analogInput(0)

def GetMoisture():
  Moisture=MoistureDetect()
  

  return Moisture[0]
def GetMoistureAndSave():
  Moisture=MoistureDetect()
  nowtime=int(time.time())
  timestamp=time.strftime("%Y-%m-%d %H:%M",time.localtime(nowtime) )
  f=open(f'{os.path.dirname(os.path.abspath(__file__))}/moistureDate',"a")
  f.write(f"Moisture,{Moisture[0]},raw,{Moisture[1]},time,{timestamp}\n")
  f.close()
  return Moisture[0]
  
