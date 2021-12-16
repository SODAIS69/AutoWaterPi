  
import os
import time


def log(logs):
    nowtime=int(time.time())
    timestamp=time.strftime("%Y-%m-%d %H:%M",time.localtime(nowtime) )
    f=open(f'{os.path.dirname(os.path.abspath(__file__))}/log.log',"a")
    f.write(f"Time: {timestamp}, Log: {logs}\n")
    f.close()