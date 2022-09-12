import netCDF4
from datetime import datetime
from netcdfToJson import netcdfToJson

if __name__ == '__main__':

#   freeze_support()
   dt = datetime.now()

# getting the timestamp

   ts1 = datetime.timestamp(datetime.now())
   nc_file = r'.\assets\ascat_20220816_081200_metopc_19582_eps_o_coa_3203_ovw.l2.nc'
   border = (40,40,67,49)
   props=['wvc_index', 'model_speed', 'model_dir', 'ice_prob', 'ice_age', 'wvc_quality_flag', 'wind_speed', 'wind_dir', 'bs_distance']
   print (" ### runing  netcdfToJson1prop")
   netcdfToJson(nc_file,r"D:\py-input-output\testGeojson2",border,props, csv= False, json= True)  #netcdfFilePath,jsonFilePath,border,property
