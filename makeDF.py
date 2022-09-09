import math
import pandas as pd
import cftime


def makeDF(xySet,ncVariables,Param):
    print(ncVariables.keys())
    print(ncVariables[Param[0]])
    print("lon", ncVariables['lon'])
    print("lat", ncVariables['lat'])
    print("time", ncVariables['time'])
    param_1 = ncVariables[Param[0]][::]
    print("len(param1):", len(param_1))
    print("len(param1[0]):", len(param_1[0]))
    param_2 = ncVariables[Param[1]][::]
    param_3 = ncVariables[Param[2]][::]
    param_4 = ncVariables[Param[3]][::]
    param_5 = ncVariables[Param[4]][::]
    param_6 = ncVariables[Param[5]][::]
    param_7 = ncVariables[Param[6]][::]
    param_8 = ncVariables[Param[7]][::]
    param_9 = ncVariables[Param[8]][::]

    longitude = ncVariables['lon'][::]

    latitude = ncVariables['lat'][::]

    time = ncVariables['time'][::]
    t_unit = ncVariables['time'].units
    print("t_unit:", t_unit)
    datevar = []
    datevar.append(cftime.num2date(time, units=t_unit, calendar="proleptic_gregorian"))
    print("len(datevar):", len(datevar))
    print("len(datevar[0]):", len(datevar))
    print("len(datevar[0][0]):", len(datevar))
    print("datevar[0][0][0]:", datevar[0][0][0])

    arr = []
    point_counter = 1
    print("len(param1:", len(param_1))
    print("len(param1[0]:", len(param_1[0]))
    print('len time:', len(time))
    print('len time[0]:', len(time[0]))

    for point in xySet:

        x = point[0]
        y = point[1]
        print("id:", point_counter)
        param1 = float(param_1[x][y])
        if math.isnan(param1):
            param1 = "nan"
        param2 = float(param_2[x][y])
        if math.isnan(param2):
            param2 = "nan"
        param3 = float(param_3[x][y])
        if math.isnan(param3):
            param3 = "nan"
        param4 = float(param_4[x][y])
        if math.isnan(param4):
            param4 = "nan"
        param5 = float(param_5[x][y])
        if math.isnan(param5):
            param5 = "nan"
        param6 = float(param_6[x][y])
        if math.isnan(param6):
            param6 = "nan"
        param7 = float(param_7[x][y])
        if math.isnan(param7):
            param7 = "nan"
        param8 = float(param_8[x][y])
        if math.isnan(param8):
            param8 = "nan"
        param9 = float(param_9[x][y])
        if math.isnan(param9):
            param9 = "nan"
        for i in datevar[0][0]:
            arr.append(
                {'id:': point_counter, 'lat:': float(latitude[x][y]), 'lon:': float(longitude[x][y]), 'time:': str(i),
                 Param[0]: param1, Param[1]: param2, Param[2]: param3, Param[3]: param4, Param[4]: param5,
                 Param[5]: param6, Param[6]: param7, Param[7]: param8, Param[8]: param9})
        point_counter += 1



        df =  pd.DataFrame.from_records(arr)
        return df




