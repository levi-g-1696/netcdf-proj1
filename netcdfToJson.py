import netCDF4
from datetime import datetime
from makeXYsetInBorder import makeXYsetInBorder, getResultSet
import numpy as np

from output import outputDataToGJson

def netcdfToJson1prop(netcdfFilePath,jsonFilePath,border,property):
   if agumentsValidation:


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