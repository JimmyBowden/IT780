#Jimmy Bowden
#IT780
#A3


import csv
from C8 import myRecommender

#-----------------------------------Variables



#-----------------------------------Functions
def readBookCSV():
    #need to extract isbn and title
    myDict = {}
    isbnList =[]
    fName = 'BX-Books.csv'
    with open(fName, 'r') as inFile:
        line = inFile.readline()
        while line != "":
        #count = 0
        #while count <50001:
            cleanLine = str.replace(line, '"', "")
            nameList  = cleanLine.split(";")
            #print(nameList)
            #if nameList[0] != '"ISBN"':
            myDict[nameList[0]] = nameList[1]
            line = inFile.readline()
            #count += 1
    #print(myList)
    return myDict

def readRatingCSV():
    myFinalDict = {}
    fName = 'BX-Book-Ratings.csv'
    with open(fName, 'r') as inFile:
        line = inFile.readline()
        count = 0
        while line != "":
        #while count < 5001:
            cleanLine = str.replace(line, '"', "")
            ratingList  = cleanLine.split(";")
            if ratingList[1] != "ISBN":
                if int(ratingList[0]) not in myFinalDict:
                    myFinalDict[int(ratingList[0])] = {}
                val = ratingList[2].strip()
                myFinalDict[int(ratingList[0])][ratingList[1]] = float(val)
            
            line = inFile.readline()
            #count = count + 1
    #print(count)
    return myFinalDict


#------------------------------------Main
myInput = input("Enter Name: ").capitalize() #276746
bookDict = readBookCSV()
#print(bookDict)
ratingDict = readRatingCSV()
#print(ratingDict)
print("Recommendations using Pearson:")
rec = myRecommender().recommend(myInput, ratingDict, 2, True)
#print(rec)
#for item in rec:
#    print(item[0], item[1])
#    print(item[0], "--->", bookDict[item[0]], "--->",item[1] )
