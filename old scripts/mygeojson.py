def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson


import json
import simplekml
import geojson
import pandas as pd

def data2kml(df):



    kml = simplekml.Kml()
    df.apply(lambda X: kml.newpoint(
            name=X["name"],
            description=unicode(X["description"].decode('utf8')),
            coords=[( X["long"], X["lat"], X["elev"])]
                                    )
            , axis=1)
    kml.save(path='map.kml')

def data2geojson(df):
    points = []
    df.apply(lambda X: points.append( (float(X["long"]),
                                       float(X["lat"]))
                                    )
            , axis=1)
    with open('map.geojson', 'w') as fp:
        geojson.dump(geojson.MultiPoint(points), fp, sort_keys=True)


col = ['lat','long','elev','name','description']
data = [[-29.9953,-70.5867,760,'A','Place a'],
        [-30.1217,-70.4933,1250,'B','Place b'],
        [-30.0953,-70.5008,1185,'C','Place c']]

df = pd.DataFrame(data, columns=col)
data2kml(df)
data2geojson(df)

#############################
# We are going to create GeoJSON file from dictionary

def df_to_geojson(dictionary):
    # create a new python dict to contain our geojson data, using geojson format
    geojson = {'type': 'FeatureCollection', 'features': []}

    # loop through each row in the dataframe
    for key, value in dictionary.items():
        # create a feature template to fill in
        feature = {'type': 'Feature',
                   'properties': {},
                   'geometry': {'type': 'Polygon',
                                'coordinates': []}}

        # fill in the coordinates
        feature['geometry']['coordinates'] = [value]

        # create properies with region id
        feature['properties']['region'] = key + 1
        # add this feature (convert dataframe row) to the list of features inside our dict
        geojson['features'].append(feature)

    return geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates":  [ -85.362709,40.466442 ]
      },
      "properties": {
        "weather":"Overcast",
        "temp":"30.2 F"
      }
    }
  ]
}

https://stackoverflow.com/questions/48586647/python-script-to-convert-csv-to-geojson


######################


import csv, json
from geojson import Feature, FeatureCollection, Point

features = []
with open('CurrentObs.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for latitude, longitude, weather, temp in reader:
        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'weather': weather,
                    'temp': temp
                }
            )
        )

collection = FeatureCollection(features)
with open("GeoObs.json", "w") as f:
    f.write('%s' % collection)


    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    import csv
    import json
    from collections import OrderedDict

    li = []
    with open('CurrentObs.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for latitude, longitude, weather, temp in reader:
            d = OrderedDict()
            d['type'] = 'Feature'
            d['geometry'] = {
                'type': 'Point',
                'coordinates': [float(latitude), float(longitude)]
            }
            d['properties'] = {
                'weather': weather,
                'temp': temp
            }
            li.append(d)

    d = OrderedDict()
    d['type'] = 'FeatureCollection'
    d['features'] = li
    with open('GeoObs.json', 'w') as f:
        f.write(json.dumps(d, sort_keys=False, indent=4))