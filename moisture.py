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

def analogInput1(channel):
    # Make sure ADC channel is 0 or 1
    if channel != 0:
        channel = 1

    # Construct SPI message
    #  First bit (Start): Logic high (1)
    #  Second bit (SGL/DIFF): 1 to select single mode
    #  Third bit (ODD/SIGN): Select channel (0 or 1)
    #  Fourth bit (MSFB): 0 for LSB first
    #  Next 12 bits: 0 (don't care)
    msg = 0b11
    msg = ((msg << 1) + channel) << 5
    msg = [msg, 0b00000000]
    reply = spi.xfer2(msg)

    # Construct single integer out of the reply (2 bytes)
    adc = 0
    for n in reply:
        adc = (adc << 8) + n

    # Last bit (0) is not part of ADC value, shift to remove it
    adc = adc >> 1

    # Calculate voltage form ADC value
    # considering the soil moisture sensor is working at 5V
    voltage = (5 * adc) / 1024

    return voltage

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
  
