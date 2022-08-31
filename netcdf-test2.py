import netCDF4
from datetime import datetime
import numpy as np

import pandas as pd

from getClosestGridPoint import getClosestGridPoint
from get_index_by_location import get_index_by_location, getXYset

dt = datetime.now()

# getting the timestamp

ts1 = datetime.timestamp(datetime.now())
nc_file = r'.\assets\ascat_20220816_081200_metopc_19582_eps_o_coa_3203_ovw.l2.nc'

nc = netCDF4.Dataset(nc_file, mode='r')

k= nc.variables.keys()

latArr = nc.variables['lat'][:]
lonArr = nc.variables['lon'][:]






#
# print( "index = ",res)
# #print ("wind dir =",wind_dir[res[0],res[1]],"  ; wind speed = " ,ws[res[0],res[1]])
# print  ("lat=",latArr[res[0],res[1]],"  :  " ,"lon=", lonArr[res[0],res[1]])
#

#
#print (wind_dir)


print ("lat 5,10", latArr[5,10] )
ts2=datetime.timestamp(datetime.now())
x= getClosestGridPoint(60.5,41.7,nc,56,40,62,44)
ts3=datetime.timestamp(datetime.now())
print ("x=",x)
print (" netcdf file opening time =",ts2-ts1 )
print (" index find time =",ts3-ts2 )