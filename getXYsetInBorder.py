import time
from datetime import datetime


from multiprocessing import Lock
import numpy as np
resultSet = set()
def getXYsetInBorder(border,latArr,lonArr,x1,x2):
  #  print ( "process ",x1,x2,"  time: ",time.perf_counter())
    latArr= np.array(latArr)
    lonArr= np.array(lonArr)

    #ts2 = datetime.timestamp(datetime.now())
   # print (x1,x2, "start time=",ts2)
    xySet= set()
    for x in range(x1, x2):
        for y in range(0, len(latArr[0])):
         #   print(x,y, "  ======")
            isInBorder = border[0] <= latArr[x, y] <= border[2]  and border[1] <= lonArr[x, y] <= border[3]
            if isInBorder: xySet.add((x, y))
    myLock= Lock()
    global resultSet
    resultSet=xySet | resultSet
    #print ("x1,x2",x1,x2,"   ",len(xySet),len (resultSet))
    #ts3=datetime.timestamp(datetime.now())
 #@   print ("process time-",x1,"-",x2, "  =", time.process_time())
    return
def getSetResult():
    global resultSet
    return resultSet


