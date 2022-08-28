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
    not_exist= (-1,-1)
    nplat = np.array(lat_arr)
    nplon = np.array(lon_arr)
    minLat= nplat.min()
    maxLat=nplon.max()
    if minLat > input_lat or input_lat >= maxLat:
        return not_exist
    minLon = nplon.min()
    maxLon = nplon.max()
    if minLon > input_lon or input_lon >= maxLon:
        return not_exist


    


