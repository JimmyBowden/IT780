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
        myFinalDict[item] = {item : {}}
    #print(myFinalDict)
    fName = 'Ratings.csv'
    with open(fName, 'r') as inFile:
        line = inFile.readline()
        while line != "":
            ratingList  = line.split(",")
            myFinalDict[ratingList[1]] = {ratingList[0] : ratingList[2].strip()}
            #print(ratingList[0], ratingList[2])
           #myList.append(nameList[0])
            line = inFile.readline()
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
sortedDictList = orderDictionary(myDict)
print(sortedDictList)
