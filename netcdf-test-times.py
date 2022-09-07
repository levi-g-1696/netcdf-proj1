import netCDF4
import time
from datetime import datetime
from makeXYsetInBorder import makeXYsetInBorder, getResultSet
import multiprocessing

if __name__ == '__main__':

#   freeze_support()
   dt = datetime.now()

# getting the timestamp

   ts1 =  time.perf_counter()
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
   border = (65,44,70,49)
   ts2= time.perf_counter()
   p1 = multiprocessing.Process(target=makeXYsetInBorder(border, latArr, lonArr, 0, 800))
   p2 = multiprocessing.Process(target=makeXYsetInBorder(border, latArr, lonArr, 801, 1600))
   p3 = multiprocessing.Process(target=makeXYsetInBorder(border, latArr, lonArr, 1601, 2400))
   p4 = multiprocessing.Process(target=makeXYsetInBorder(border, latArr, lonArr, 2401, 3200))
   print ("p1 start time:",time.perf_counter())
   p1.start()
   print ("p2 start time:",time.perf_counter())
   p2.start()
   print ("p3 start time:",time.perf_counter())
   p3.start()
   print ("p4 start time:",time.perf_counter())
   p4.start()


#
#print (wind_dir)

   p1.join()
   print ("p1 join time:",time.perf_counter())
   p2.join()
   print ("p2 join time:",time.perf_counter())
   p3.join()
   print ("p3 join time:",time.perf_counter())
   p4.join()
   print ("p4 join time:",time.perf_counter())
   ts3 = time.perf_counter()

   print (" netcdf file opening time =",ts2-ts1 )
   print (" border indexes set was found by multiprocess x4 for: ",ts3-ts2 ,"sec")

   ts4= time.perf_counter()
   p= makeXYsetInBorder(border, latArr, lonArr, 0, len(latArr))
   ts5= time.perf_counter()
   res= getResultSet()
   print (res)
   print ("border indexes set was found by 1 process for:",ts5-ts4,"sec")
###############



