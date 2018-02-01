#C2 
#Jimmy Bowden
#It780
from math import *
from tables import *
#------------Variables--------------------
c1 = -42.379
c2 = 2.04901523
c3 = 10.14333127
c4 = -0.22475541
c5 = -6.83783 * pow(10,-3)
c6 = -5.481717 * pow(10,-2)
c7 = 1.22874 * pow(10,-3)
c8 = 8.5282 * pow(10,-4)
c9 = -1.99 * pow(10,-6)

#-----------Functions----------------------
def celsToFer(cels):
    fer = 32 + cels * 1.8
    fer = round(fer, 2)
    return fer 

def ferWindChill(fer, windVel):
    if fer > 50:
        windChillTemp = "X"
    else:
        windChillTemp = 35.74 + (0.6215 * fer) - (35.75 * pow(windVel, 0.16)) + (0.4275 * fer * pow(windVel, 0.16))
        windChillTemp = round(windChillTemp, 2)
    return windChillTemp

def ferHumidity(T, R):
    if T < 80:
        humTemp = "X"
    else:
        humTemp = c1 + (c2 * T) + (c3 * R) + (c4 * T * R) + (c5 * T * T) + (c6 * R * R) + (c7 * T * T * R) + (c8 * T * R * R) + (c9 * T * T  * R * R)
        humTemp = round(humTemp, 2)
    #print(humTemp)
    return humTemp

def makeList(inTup):
    columnList = []
    firstRange = inTup[0]
    secondRange = inTup[1]
    while firstRange <= secondRange:
        innerFirstRange = 5
        rowList = []
        rowList.append(firstRange)
        myFer = celsToFer(firstRange)
        rowList.append(myFer)
        while innerFirstRange < 41:
            windChillTemp = ferWindChill(myFer, innerFirstRange)
            rowList.append(windChillTemp)
            innerFirstRange = innerFirstRange + 5
        columnList.append(rowList)
        firstRange = firstRange + 1
    #print(columnList)
    return columnList

def makeHumidtyList(inTup):
    columnList = []
    firstRange = inTup[0]
    secondRange = inTup[1]
    while firstRange <= secondRange:
        innerFirstRange = 4
        rowList = []
        rowList.append(firstRange)
        myFer = celsToFer(firstRange)
        rowList.append(myFer)
        while innerFirstRange < 11:
            perNum = .1 * innerFirstRange
            #print(perNum)
            humTemp = ferHumidity(myFer, perNum)
            rowList.append(humTemp)
            innerFirstRange = innerFirstRange + 1
        columnList.append(rowList)
        firstRange = firstRange + 1
        #print(columnList)
    return columnList

def getInput():
    while True:
        try:
            inVal1, inVal2 = input("Enter two different numbers between -20 and 50 (Space delimated): ").split()
            inVal1 = int(inVal1)
            inVal2 = int(inVal2)
            if inVal1  < 51 and inVal1 > -21:
                pass
            else:
                raise ValueError("The first number isn't in range.")
            if inVal2  < 51 and inVal2 > -21:
                pass
            else:
                raise ValueError("The second number isn't in range.")
            if inVal1 == inVal2:
                raise ValueError("Cannot have two of the same values.")
            endTup = (inVal1, inVal2)
            return endTup
            break
        except Exception as error:
            print(error)

def makeWindTable(inList):
    titleString = "Wind Chill Temperatures"
    headerString = "Cels  Fahr  5mph  10mph 15mph 20mph 25mph 30mph 35mph 40mph"
    print(titleString)
    print(headerString)
    for i in inList:
        print(str(i[0]).ljust(6) + str(i[1]).ljust(6) + str(i[2]).ljust(6) + str(i[3]).ljust(6) + str(i[4]).ljust(6) + str(i[5]).ljust(6) + str(i[6]).ljust(6) + str(i[7]).ljust(6) + str(i[8]).ljust(6) + str(i[9]).ljust(6))

def makeHumTable(inList):
    titleString = "Heat Index Temperatures"
    headerString = "Cels  Fahr  40%   50%   60%   70%   80%   90%   100% "
    print(" ")
    print(titleString)
    print(headerString)
    for i in inList:
        print(str(i[0]).ljust(6) + str(i[1]).ljust(6) + str(i[2]).ljust(6) + str(i[3]).ljust(6) + str(i[4]).ljust(6) + str(i[5]).ljust(6) + str(i[6]).ljust(6) + str(i[7]).ljust(6) + str(i[8]).ljust(6))
       

#------------Main--------------------------
#test = celsToFer(10)
#chill = ferWindChill(test, 5)
#print(chill)
myInput = getInput()
myList = makeList(myInput)
makeWindTable(myList)
myHumList = makeHumidtyList(myInput)
makeHumTable(myHumList)
