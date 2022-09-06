import csv
import json
from collections import OrderedDict
def outputDataToGJson(pointSet,latArr,lonArr,propNames,propValueArrs,filePath):
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
    return

