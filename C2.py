#C2 
#Jimmy Bowden
#It780
from math import *
from tables import *
#------------Variables--------------------



#-----------Functions----------------------
def celsToFer(cels):
    fer = 32 + cels * 1.8
    fer = round(fer, 2)
    return fer 

def ferWindChill(fer, windVel):
    windChillTemp = 35.74 + (0.6215 * fer) - (35.75 * pow(windVel, 0.16)) + (0.4275 * fer * pow(windVel, 0.16))
    windChillTemp = round(windChillTemp, 2)
    return windChillTemp

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
    headerString = "Celsius Fahr   5mph    10mph   15mph   20mph   25mph   30mph   35mph   40mph"
    for i in inList:
       

#------------Main--------------------------
#test = celsToFer(10)
#chill = ferWindChill(test, 5)
#print(chill)
myInput = getInput()
myList = makeList(myInput)
makeWindTable(myList)