#Jimmy Bowden
#IT780
#C4


import csv


#-----------------Var


#-----------------Functions
def readNameCSV():
    myList = []
    fName = 'People.csv'
    with open(fName, 'r') as inFile:
        line = inFile.readline()
        while line != "":
            nameList  = line.split(",")
            myList.append(nameList[0])
            line = inFile.readline()
    #print(myList)
    return myList

def readRatingCSV(nameList):
    myRatingDict = {}
    myFinalDict = {}
    for item in nameList:
        myFinalDict[item] = {}
    #print(myFinalDict)
    fName = 'Ratings.csv'
    with open(fName, 'r') as inFile:
        line = inFile.readline()
        count = 0
        while line != "":
            ratingList  = line.split(",")
            val = ratingList[2].strip()
            myFinalDict[ratingList[1]][ratingList[0]] = float(val)
            #myFinalDict[ratingList[1]] ({ratingList[0] : float(val)})
            #print(ratingList[0], ratingList[2])
           #myList.append(nameList[0])
            line = inFile.readline()
            count = count + 1
    #print(count)
    return myFinalDict

def orderDictionary(myDict):
    myDictList = []
    for key in myDict:
        temp = ()
        temp = [myDict[key], key[0]]
        myDictList.append(temp)
    sortedDictList = sorted(myDictList, reverse=True)
    return sortedDictList

#-----------------Main
dictList = readNameCSV()
myDict = readRatingCSV(dictList)
#sortedDictList = orderDictionary(myDict)
#print(myDict)
