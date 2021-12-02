import time
from picamera import PiCamera
import os

camera = PiCamera()
nowtime=int(time.time())
timestamp=time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(nowtime) )
camera.capture(f'{os.path.dirname(os.path.abspath(__file__))}/Captured/{timestamp}.jpg') #取script路徑+資料夾