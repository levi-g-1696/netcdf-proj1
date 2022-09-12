import csv
import json
from collections import OrderedDict

def outputDataToGJson(pointSet,latArr,lonArr,propNames,propValueArrs,filePath):

#   updated from source https://stackoverflow.com/questions/48586647/python-script-to-convert-csv-to-geojson
#    function: write set of points to geojson file
#    args:
#       pointSet: set of tuples (x,y) indexes in latArr,lonArr fit to border condition
#       latArr,lonArr : numpy.ndarray, latitude and longitude vals  extracted from netcdf file
#       propNames:  list of strings , property name , like this ['wind_dir'], only property[0] will be inputed
#       propValueArrs: list of arrays numpy.ndarray, every element of the list is array of property value for
#                       appropriate point. only option of 1 property is implemented in this version. only propValueArrs[0]
#                       will be imputed
#       filePath:  string, full json file path for output, will be overwriten if exist
#    result: geojson file at filePath
  if argsValidation():
    li = []
    propName= propNames[0]
    values= propValueArrs[0]

    for point in pointSet:
        x=point[0]
        y= point[1]

        latitude= latArr[x][y]
        longitude= lonArr[x][y]

        d = OrderedDict()
        d['type'] = 'Feature'
        d['geometry'] = {
            'type': 'Point',
            'coordinates': [float(latitude), float(longitude)]
        }
        d['properties'] = {
            propNames[0]: values[x][y]
           
        }
        li.append(d)

    d = OrderedDict()
    d['type'] = 'FeatureCollection'
    d['features'] = li
    f = open(filePath, "w")
    f.write(json.dumps(d, sort_keys=False, indent=4))
    f.close()
###################################################################################################

def argsValidation(): return True


def outputDataToGJson_V2(dataFrame,outfile ):

    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [d["lon:"], d["lat:"]],
                },
                "properties": d,
            } for d in dataFrame]
    }

    output = open(outfile, 'w')
    json.dump(geojson, output)

    return

def outputDataToGJson_V3(dataFrame,outfile ):
    j1= dataFrame.to_json(orient="records")
    jObj= json.loads(j1)

    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [d["lon:"], d["lat:"]],
                },
                "properties": d,
            } for d in jObj]
    }

    output = open(outfile, 'w')
    json.dump(geojson, output)

    return
