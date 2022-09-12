import math
import pandas as pd
import cftime
import numpy as np


def getDF(xySet, ncVariables, Param):
    #function: creates pandas dataframe from set of points
    #args:
   #   xySet: set of netcdf file indexes that fits the conditions of border
   #   ncVariables: nc.variables of netcdf file
   #   Param: list of strings, property list for point like this ['wvc_index', 'model_speed', 'model_dir', 'ice_prob', 'ice_age', 'wvc_quality_flag', 'wind_speed', 'wind_dir', 'bs_distance']
    #result: dataframe object

    print(ncVariables.keys())
    paramValDict= {}
    valuesDict= {}
    for p in Param:
       paramValDict[p] = np.array(ncVariables[ p] [::])

  #  print(ncVariables[Param[0]])
    print("lon", ncVariables['lon'])
    print("lat", ncVariables['lat'])
    print("time", ncVariables['time'])

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
 #       print(pointProps1)
        point_counter += 1
        arr.append(pointProps1)
    print("point counter=", point_counter)
    df =  pd.DataFrame.from_dict(arr)
  #  print (arr)

    return df




