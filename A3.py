#Jimmy Bowden
#IT780
#A3


import csv
#import C8

#-----------------------------------Variables



#-----------------------------------Functions
def readBookCSV():
    #need to extract isbn and title
    myDict = {}
    fName = 'BX-Books.csv'
    with open(fName, 'r') as inFile:
        line = inFile.readline()
        #while line != "":
        count = 0
        while count <1001:
            nameList  = line.split(";")
            print(nameList)
            myDict[nameList[0]] = nameList[1]
            line = inFile.readline()
            count += 1
    #print(myList)
    return myDict

def readRatingCSV(nameList):
    myRatingDict = {}
    myFinalDict = {}
    for item in nameList:
        myFinalDict[item] = {}
    #print(myFinalDict)
    fName = 'BX-Book-Ratings.csv'
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


#------------------------------------Main
bookList = readBookCSV()
print(bookList)
