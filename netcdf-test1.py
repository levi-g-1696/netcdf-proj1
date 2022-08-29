import netCDF4
from datetime import datetime
import numpy as np

import pandas as pd

from get_index_by_location import get_index_by_location, getXYset

dt = datetime.now()

# getting the timestamp

ts1 = datetime.timestamp(datetime.now())
nc_file = r'D:\py-input-output\ascat_20220816_081200_metopc_19582_eps_o_coa_3203_ovw.l2.nc'
nc = netCDF4.Dataset(nc_file, mode='r')

k= nc.variables.keys()

lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time_var = nc.variables['time']
dtime = netCDF4.num2date(time_var[:],time_var.units)
wind_dir = np.array(nc.variables['wind_dir'][:])
ws= np.array(nc.variables['wind_speed'][:])
print ("wind dir =",wind_dir[0,1],"  ; wind speed = " ,ws[0,6])
ts2=datetime.timestamp(datetime.now())
res= get_index_by_location(4.165,192.03, lat,lon)
print( "+++",res)
ts3=datetime.timestamp(datetime.now())

#
#print (wind_dir)
print (" alapsed time =",ts2-ts1 )
print (" alapsed time2 =",ts3-ts2 )
# a pandas.Series designed for time series of a 2D lat,lon grid
#wind_ts = pd.Series(wind_dir, index=dtime)

#wind_ts.to_csv('D:\py-input-output\wind.csv',index=True, header=True)