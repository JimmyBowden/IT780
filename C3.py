#C3
#Jimmy Bowden
#IT780

#------------Variables-----------------



#------------Functions-----------------
def getInput():
    while True:
        try:
            inVal = input("Enter a sentence: ")
            if inVal.strip() != "":
                pass
            else:
                raise ValueError("There was nothing entered.")

            return inVal
            break
        except Exception as error:
            print(error)


def makeDictionary(inString):
    myDict = {}
    for char in inString:
        if char in myDict:
            myDict[char] += 1
        elif char == " ":
            pass
        else:
            myDict[char] = 1
    return myDict


def orderDictionary(myDict):
    myDictList = []
    for key in myDict:
        temp = ()
        temp = [myDict[key], key]
        myDictList.append(temp)
    sortedDictList = sorted(myDictList, reverse=True)
    #print(sortedDictList)
    return sortedDictList


def printDictionary(myDictList):
    for i in myDictList:
        print(i[1] + ": " + str(i[0]))

#------------Main----------------------
myInput = getInput()
myDict = makeDictionary(myInput)
myDictList = orderDictionary(myDict)
printDictionary(myDictList)
