def getXYsetInBorderOLD(border,latArr,lonArr):
    #border (latmin,lonmin , latmax, lonmax)
    xySet= set()
    pointA= getClosestGridPoint(border[0], border[1])
    pointB=  getClosestGridPoint(border[0], border[3])
    pointC=  getClosestGridPoint(border[2], border[3])
    pointD=  getClosestGridPoint(border[2], border[1])
    xA= pointA[0]
    xB= pointB[0]
    xC= pointC[0]
    xD= pointD[0]
    yA = pointA[1]
    yB = pointB[1]
    yC = pointC[1]
    yD = pointD[1]
    #there are 4 options  for satellite walking direction 31 13 24 42
    #   1 2
    #   4 3
    #

    if xA-1>=0 : # index validation
      option31= latArr(xA,yA)-latArr(xA-1,yA) >0 and lonArr(xA,yA)-lonArr(xA-1,yA) <0
      option13= latArr(xA,yA)-latArr(xA-1,yA) <0 and lonArr(xA,yA)-lonArr(xA-1,yA) >0
      option42= latArr(xA,yA)-latArr(xA-1,yA) >0 and lonArr(xA,yA)-lonArr(xA-1,yA) >0
      option24= latArr(xA,yA)-latArr(xA-1,yA) <0 and lonArr(xA,yA)-lonArr(xA-1,yA) <0

    else :
       option31 = latArr(xA+1, yA) - latArr(xA , yA ) > 0 and lonArr(xA+1, yA) - lonArr(xA , yA ) < 0
       option13 = latArr(xA+1, yA) - latArr(xA , yA ) < 0 and lonArr(xA+1, yA) - lonArr(xA , yA ) > 0
       option42 = latArr(xA+1, yA) - latArr(xA , yA ) > 0 and lonArr(xA+1, yA) - lonArr(xA , yA ) > 0
       option24 = latArr(xA+1, yA) - latArr(xA , yA ) < 0 and lonArr(xA+1, yA) - lonArr(xA , yA ) < 0

    if option31:
        x1= xB
        x2=xD
        y1 =yA
        y2=yC
    elif option13:
        x1= xD
        x2= xB
        y1= yC
        y2 = yA
    elif option42:
        x1 = xA
        x2 = xA
        y1 = yD
        y2 = yB
    else: # option24:
        x1 = xC
        x2 = xC
        y1 = yB
        y2 = yD

    for x in range (x1,x2):
        for y in range(y1,y2):
            if isInBorder(border,x,y,latArr,lonArr): xySet.add((x,y))

    return xySet


def isInBorder(border,x,y,latArr,lonArr) :
    res= False
    if border[0] <= latArr[x,y] <= border[2]:
        if border[1] <= lonArr[x,y] <= border[3]:
            res =True

    return res