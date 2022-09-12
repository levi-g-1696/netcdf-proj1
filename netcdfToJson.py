import netCDF4
from datetime import datetime

from makeDF import getDF
from makeXYsetInBorder import makeXYsetInBorder, getResultSet
import numpy as np
import pandas as pd

from output import outputDataToGJson,outputDataToGJson_V3

def netcdfToJson(netcdfFilePath,jsonFilePath,border,property,csv,json):
    # function : makes GeoJson file from netcdf file data according the border for 1 physical property
    #            (pilot version). it is a wrap for makeXYsetInBorder() getResultSet() outputDataToGJson() .
    #  arguments:
    #    netcdfFilePath: string, full netcdf file path
    #    jsonFilePath: string, full json file path for output, will be overwriten if exist
    #    border: tuple (latidude_min, longitude_min, latitude_max,longitude_max)
   #     csv: boolean , true if need to create csv  output file
    #    json: boolean , true if need to create json output file
    #    property: list of strings, property list for point like this
    #              ['wvc_index', 'model_speed', 'model_dir', 'ice_prob', 'ice_age', 'wvc_quality_flag', 'wind_speed', 'wind_dir', 'bs_distance']
    #    dependences warning: agumentsValidation() - boolean. must be implemented. returns true in this version.
    # result: geojson file at jsonFilePath and\or csv file
   if agumentsValidation():


     nc = netCDF4.Dataset(netcdfFilePath, mode='r')
     latArr = np.array(nc.variables['lat'][:])
     lonArr = np.array(nc.variables['lon'][:])
     makeXYsetInBorder(border, latArr, lonArr, 0, len(latArr))
     myset=  getResultSet()
     resultDataFrame= getDF(myset, nc.variables, property)
     print (resultDataFrame)
     if csv :  resultDataFrame.to_csv(jsonFilePath +".csv")
     if json: outputDataToGJson_V3(resultDataFrame,jsonFilePath +".json")

     print (myset)


def agumentsValidation():  #must implementation
    return True