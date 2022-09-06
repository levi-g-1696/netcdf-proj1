import netCDF4
from datetime import datetime
from getXYsetInBorder import getXYsetInBorder, getSetResult
import numpy as np

from output import outputDataToGJson

if __name__ == '__main__':

#   freeze_support()
   dt = datetime.now()

# getting the timestamp

   ts1 = datetime.timestamp(datetime.now())
   nc_file = r'.\assets\ascat_20220816_081200_metopc_19582_eps_o_coa_3203_ovw.l2.nc'

   nc = netCDF4.Dataset(nc_file, mode='r')



   latArr = nc.variables['lat'][:]
   lonArr = nc.variables['lon'][:]
   wind_dir_vals = np.array(nc.variables['wind_dir'][:])
   border = (62,45,67,49)
   ts2=datetime.timestamp(datetime.now())

################################################

   # myset=set()
   # myset.add((0,0))
   # myset.add((0,1))
   # myset.add((0,2))
   # myset.add((1,0))
   # myset.add((1,1))
   # myset.add((1,2))
   # latArr= [[33.12,33.33,33.40],[33.20,33.55,33.77]]
   # lonArr= [[13.12,13.33,33.40],[13.20,13.55,13.77]]
   # print("test")
   # print (latArr[0][1])
   # WDvals= [[10.12,10.33,9.40],[9.20,9.55,9.77]]



   getXYsetInBorder(border,latArr,lonArr,0,3200)
   myset=  getSetResult()


   print (myset)
   outputDataToGJson(myset, latArr, lonArr, ["wind_dir"], [wind_dir_vals])
