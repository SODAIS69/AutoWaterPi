import time
from picamera import PiCamera
import os
import gallery

camera = PiCamera()
nowtime=int(time.time())
camera.resolution = (1640, 1232)
timestamp=time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(nowtime) )
camera.capture(f'{os.path.dirname(os.path.abspath(__file__))}/Captured/{timestamp}.jpg') #取script路徑+資料夾
gallery.GenerateGallery()