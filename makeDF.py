import math
import pandas as pd
import cftime
import numpy as np


def getDF(xySet, ncVariables, Param):
    print(ncVariables.keys())
    paramValDict= {}
    valuesDict= {}
    for p in Param:
       paramValDict[p] = np.array(ncVariables[ p] [::])

  #  print(ncVariables[Param[0]])
    print("lon", ncVariables['lon'])
    print("lat", ncVariables['lat'])
    print("time", ncVariables['time'])

 #   param_1 = ncVariables[Param[0]][::]
 #    print("len(param1):", len(param_1))
 #    print("len(param1[0]):", len(param_1[0]))
  #  param_2 = ncVariables[Param[1]][::]
  #  param_3 = ncVariables[Param[2]][::]
  #   param_4 = ncVariables[Param[3]][::]
  #   param_5 = ncVariables[Param[4]][::]
  #   param_6 = ncVariables[Param[5]][::]
  #   param_7 = ncVariables[Param[6]][::]
  #   param_8 = ncVariables[Param[7]][::]
  #   param_9 = ncVariables[Param[8]][::]

    longitude = np.array(ncVariables['lon'][::])

    latitude =  np.array(ncVariables['lat'][::])

    time =( ncVariables['time'][::])
    t_unit = (ncVariables['time'].units)
    print("t_unit:", t_unit)
    datevar = []
    datevar.append(cftime.num2date(time, units=t_unit, calendar="proleptic_gregorian"))
    print("len(datevar):", len(datevar))
    print("len(datevar[0]):", len(datevar))
    print("len(datevar[0][0]):", len(datevar))
    print("datevar[0][0][0]:", datevar[0][0][0])

    arr = []
    point_counter = 1
 #   print("len(param1:", len(paramValues[1]))
 #   print("len(param1[0]:", len(paramValues[1][0]))
    print('len time:', len(time))
    print('len time[0]:', len(time[0]))

    for point in xySet:

        x = point[0]
        y = point[1]
        pointDict={}
        for p in Param:
            paramArr= paramValDict[p]
            paramval= float(paramArr[x][y])

            if math.isnan(paramval):
                paramval = "nan"
            pointDict[p]=paramval

        pointProps= {'id:': point_counter, 'lat:': float(latitude[x][y]), 'lon:': float(longitude[x][y]), 'time:': str(datevar[0][0][0])}
      #  print ((pointDict))
        pointProps1= pointProps | pointDict
        print(pointProps1)
        point_counter += 1
        arr.append(pointProps)
    print("point counter=", point_counter)
    df =  pd.DataFrame.from_dict(arr)
    print (arr)

    return df




