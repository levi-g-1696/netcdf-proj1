import time
from datetime import datetime


from multiprocessing import Lock
import numpy as np
resultSet = set()
def makeXYsetInBorder(border, latArr, lonArr, x1, x2):
    # function: makes set of netcdf file indexes that fits the conditions of border
    # arguments:
    #  border: tuple (latidude_min, longitude_min, latitude_max,longitude_max)
    #  latArr latitude 2D-list extracted from netcdf file
    #  lonArr longitude 2D-list extracted from netcdf file
    #  x1 x2 integers, first and last rows indexes in latArr and lonArr for search
    # result: set on global variable resultSet ( does not returns any value)
    # the result may read by  getResultSet()

    latArr= np.array(latArr)
    lonArr= np.array(lonArr)
    global resultSet

    xySet= set()
    for x in range(x1, x2):
        for y in range(0, len(latArr[0])):
         #   print(x,y, "  ======")
            isInBorder = border[0] <= latArr[x, y] <= border[2]  and border[1] <= lonArr[x, y] <= border[3]
            if isInBorder: xySet.add((x, y))
    myLock= Lock()
    with myLock:
      resultSet=xySet | resultSet
    #print ("x1,x2",x1,x2,"   ",len(xySet),len (resultSet))
    #ts3=datetime.timestamp(datetime.now())
 #@   print ("process time-",x1,"-",x2, "  =", time.process_time())
    return


def getResultSet():
    global resultSet
    return resultSet




