import netCDF4
from datetime import datetime
from netcdfToJson import netcdfToJson1prop

if __name__ == '__main__':

#   freeze_support()
   dt = datetime.now()

# getting the timestamp

   ts1 = datetime.timestamp(datetime.now())
   nc_file = r'.\assets\ascat_20220816_081200_metopc_19582_eps_o_coa_3203_ovw.l2.nc'
   border = (62,45,67,49)

   print (" ### runing  netcdfToJson1prop")
   netcdfToJson1prop(nc_file,r"D:\py-input-output\testGeojson.json",border,'wind_dir', csv= False, json= True)  #netcdfFilePath,jsonFilePath,border,property
