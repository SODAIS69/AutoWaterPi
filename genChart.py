from typing import TextIO
import numpy as np
from numpy.core.records import array
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
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
        print(strarray)
        moisture.append(strarray[1])
        raw.append(strarray[3])
        time.append(strarray[5])
        

    if (len(moisture)>40):
        del moisture[:30]
        del raw[:30]
        del time[:30]
    print(moisture)



    dic={
        "moisture":moisture,
        "raw":raw,
        "time":time
    }
    df=pd.DataFrame(dic)
    #print(moisture)
    #print(raw)
    #print(time)

    #x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
    #x = x.to_timestamp().to_pydatetime()
    ## 產生三組，每組 200 個隨機常態分布元素
    #y = np.random.randn(200, 3).cumsum(0)
    #ccc broder
    #plt.figure(figsize=(4,9))
    plt.plot(df.time, df.moisture, color="#62879e")
    plt.xlabel('DateTime')
    plt.xticks(df.time, rotation='vertical')
    plt.ylabel("Moisture (%)")
    plt.gca().invert_yaxis()

    plt.title('Moisture')

    #plt.show()
    plt.savefig(f'{os.path.dirname(os.path.abspath(__file__))}/Captured/moisture.jpg', bbox_inches='tight')