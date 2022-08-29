#       get_index_by_location (input_lat , input_lon, lat_arr,lon_arr)

# input :location
#output:  index (x,y)  in netcdf file if exist as  tuple
#          if not exist returns (-1,-1)
#algorythm: if (input_lat or input_lon out of lat or lon range in the file)
#              { return (-1,-1)}
#           else {   run processA to find set lat_set of lat_arr[i,j] <= input_lat < lat_arr[i,j+1]
#                 in parallel with processB to find set lon_set of lon_arr[i,j] <= input_lon < lon_arr[i,j+1]
#                result_set= lat_set & lon_set
#                result_tuple= (-1,-1)
#                if  (result_set is not empty) result_tuple= result_set element
#                return result_tuple
import numpy as np
def get_index_by_location (input_lat , input_lon, lat_arr,lon_arr):
    notExist= (-1,-1)
    npLat = np.array(lat_arr)
    npLon = np.array(lon_arr)
    minLat= npLat.min()
    maxLat=npLon.max()
    if minLat > input_lat or input_lat >= maxLat:
        return notExist
    minLon = npLon.min()
    maxLon = npLon.max()
    if minLon > input_lon or input_lon >= maxLon:
        return notExist
    setLat= getXYset(npLat,input_lat)
    print (setLat)
    setLon = getXYset(npLon, input_lon)
    print (setLon)
    setResult= setLat & setLon
    result= notExist
    if len(setResult)>0:
      result= setResult.pop();
    return (result)


def getXYset(values,myvalue):
    xySet= set()
    for i in range (len(values)):
       # for j in range (len(values[i]-2)):
        for j in range(81):
            if values[i,j] <= myvalue <= values[i,j+1]:
            # if values[i, j] == myvalue :
                xySet.add((j,i))
    return xySet




    


