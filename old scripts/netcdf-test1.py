import netCDF4
from datetime import datetime
import numpy as np

import pandas as pd

from getClosestGridPoint import getClosestGridPoint
from get_index_by_location import get_index_by_location, getXYset

dt = datetime.now()

# getting the timestamp

ts1 = datetime.timestamp(datetime.now())
nc_file = r'../assets/ascat_20220816_081200_metopc_19582_eps_o_coa_3203_ovw.l2.nc'
lat=3.971
lon= 191.706
print( "lat,lon= ",lat,lon)
nc = netCDF4.Dataset(nc_file, mode='r')

k= nc.variables.keys()

latArr = nc.variables['lat'][:]
lonArr = nc.variables['lon'][:]
time_var = nc.variables['time']
dtime = netCDF4.num2date(time_var[:],time_var.units)
wind_dir = np.array(nc.variables['wind_dir'][:])
ws= np.array(nc.variables['wind_speed'][:])

ts2=datetime.timestamp(datetime.now())

res= get_index_by_location(lat,lon, latArr,lonArr)
ts3=datetime.timestamp(datetime.now())
print( "index = ",res)
print (latArr)
#print ("wind dir =",wind_dir[res[0],res[1]],"  ; wind speed = " ,ws[res[0],res[1]])
print  ("lat=",latArr[res[0],res[1]],"  :  " ,"lon=", lonArr[res[0],res[1]])


#
#print (wind_dir)
print (" netcdf file opening time =",ts2-ts1 )
print (" index find time =",ts3-ts2 )
print ("lat 5,10", latArr[5,10] )
x= getClosestGridPoint(59.8,42.7,nc,56,40,62,44)
print ("x=",x)
# a pandas.Series designed for time series of a 2D lat,lon grid
#wind_ts = pd.Series(wind_dir, index=dtime)

#wind_ts.to_csv('D:\py-input-output\wind.csv',index=True, header=True)