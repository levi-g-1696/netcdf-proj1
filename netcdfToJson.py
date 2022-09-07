import netCDF4
from datetime import datetime
from makeXYsetInBorder import makeXYsetInBorder, getResultSet
import numpy as np

from output import outputDataToGJson

def netcdfToJson1prop(netcdfFilePath,jsonFilePath,border,property):
    # function : makes GeoJson file from netcdf file data according the border for 1 physical property
    #            (pilot version). it is a wrap for makeXYsetInBorder() getResultSet() outputDataToGJson() .
    #  arguments:
    #    netcdfFilePath: string, full netcdf file path
    #    jsonFilePath: string, full json file path for output, will be overwriten if exist
    #    border: tuple (latidude_min, longitude_min, latitude_max,longitude_max)
    #    property: list of strings , property name , like this ['wind_dir'], only property[0] will be inputed
    #    dependences warning: agumentsValidation() - boolean. must be implemented. returns true in this version.
    # result: geojson file at jsonFilePath
   if agumentsValidation():


     nc = netCDF4.Dataset(netcdfFilePath, mode='r')
     latArr = np.array(nc.variables['lat'][:])
     lonArr = np.array(nc.variables['lon'][:])
     propVals = np.array(nc.variables[property][:])



     makeXYsetInBorder(border, latArr, lonArr, 0, len(latArr))
     myset=  getResultSet()

     print (myset)
     outputDataToGJson (myset, latArr, lonArr, [property], [propVals],jsonFilePath)

def agumentsValidation():  #must implementation
    return True