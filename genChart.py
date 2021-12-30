from typing import TextIO
import numpy as np
from numpy.core.records import array
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import os
import datetime as dt
def GenerateMoistureChart():
    f=open('/home/pi/AutoWater/moistureDate',"r")
    moisture=[]
    raw=[]  
    time=[]
    while True:
        nstr=f.readline()
        #print(nstr)
        if len(nstr) == 0:
            break
        strarray=nstr.split(",")
        #print(strarray)
        moisture.append(strarray[1])
        raw.append(strarray[3])
        time.append(strarray[5])
        
    # print(len(moisture)) #only shows data for five days
    lens=len(moisture)-1440

    if (len(moisture)>1440):
        del moisture[:lens]
        del raw[:lens]
        del time[:lens]
        print(len(moisture))
        print(len(raw))
        print(time)

    #print(moisture)

    
    

    moisture=list(map(int, moisture))
    raw=list(map(int, raw))

    time=[dt.datetime.strptime(d,'%Y-%m-%d %H:%M\n') for d in time]
    #print(time)
    dic={
        "moisture":moisture,
        "raw":raw,
        "time":time
    }

    testpour={
        "time":["2021-12-12 01:34\n","2021-12-12 01:34\n"],
        "point":[20,30]
    }
    df=pd.DataFrame(dic)
    df_test=pd.DataFrame(testpour)
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M\n'))
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(df.time, df.moisture, color="#62879e")
    
    plt.xlabel('DateTime')
    #plt.xticks(df.time, rotation='vertical')
    plt.ylabel("Moisture (%)")
   # plt.gca().invert_yaxis() 反轉Y軸

    #plt.plot(df_test.time,df_test.point)
    
    plt2=plt.twinx()
    
    plt.title('Moisture')
    plt.legend(loc = 'lower left')
    
    plt2.set_ylabel("Raw Data")
    
    plt2.plot(df.time,df.raw,color="#fcba03")
    #plt2.invert_yaxis()
    

    plt2.legend(loc= 0)
    
    plt.gcf().autofmt_xdate()
   
    
    #plt.show()
    plt.savefig(f'{os.path.dirname(os.path.abspath(__file__))}/Captured/moisture.jpg', bbox_inches='tight')