

def getClosestGridPoint(lat,lon, netcdfDataset,latmin,lonmin,latMax,lonMax):
    global nc
    nc = netcdfDataset
    latArr = nc.variables['lat'][:]
    lonArr = nc.variables['lon'][:]
    pointA= (0,0)
    pointB= (0,1)
    k= 1.1

    latGridVal= (latArr[pointB[0],pointB[1]] - latArr[pointA[0],pointA[1]])*k
    lonGridVal = (lonArr[pointB[0], pointB[1]] - lonArr[pointA[0], pointA[1]]) * k

    mayBePointsByLat= getXYsetCloseToPoint(latGridVal,latArr,lat)
    print("may be lat=", len(mayBePointsByLat))
    mayBePointsByLon = getXYsetCloseToPoint(lonGridVal, lonArr, lon)
    print("may be lon=", len(mayBePointsByLon))
    mayBeClosePoints= mayBePointsByLat & mayBePointsByLon
    print("may be close=", len(mayBeClosePoints))

    mayBeClosePoints= RemoveNotInBorder(mayBeClosePoints,latmin,lonmin, latMax,lonMax)


    return mayBeClosePoints.pop()
def getXYsetCloseToPoint(rangeVal,values,myvalue):
    xySet= set()
    for i in range (len(values)):
       # for j in range (len(values[i]-2)):
        for j in range(81 ):
            mmin=myvalue -rangeVal
            mplus=myvalue + rangeVal
            if values[i,j] > myvalue -rangeVal and values[i,j] < myvalue + rangeVal:
                xySet.add((i,j))
    return xySet 

def RemoveNotInBorder(mayBeClosePoints,latmin,lonmin, latMax,lonMax):
    xySet = set()
    latArr = nc.variables['lat'][:]
    lonArr = nc.variables['lon'][:]
    for point in mayBeClosePoints:
        if latmin <= latArr[point[0], point[1]] <= latMax:
            if    lonmin<= lonArr[point[0], point[1]]<= lonMax:
                 xySet.add(point)
    return xySet

def latValueByIndx(point):
    latArr = nc.variables['lat'][:]
    return latArr[point[0], point[1]]

def lonValueByIndx(point):

    lonArr = nc.variables['lon'][:]
    return lonArr[point[0], point[1]]