#Jimmy Bowden
#IT780 C1


from math import *
#---------------Variable---------------





#---------------Function---------------

def getInput():
    while True:
        try:
            inVal1, inVal2 = input("Enter two different numbers between 0 and 360 (Space delimated): ").split()
            inVal1 = int(inVal1)
            inVal2 = int(inVal2)
            if inVal1  < 361 and inVal1 > -1:
                pass
            else:
                raise ValueError("The first number isn't in range.")
            if inVal2  < 361 and inVal2 > -1:
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


#flips the #'s to have small first then large returns that as tuple
def flipFlop(inTup):
    in1 = inTup[0]
    in2 = inTup[1]
    if in1 > in2:
        return1 = in2
        return2 = in1
    else:
        return1 = in1
        return2 = in2
    outTup = (return1, return2)
    return outTup


def doTrig(inTup):
    in1 = inTup[0]
    in2 = inTup[1]
    forIn1 = in1 / 5
    forIn2 = in2 / 5
    forLim = forIn2 - forIn1
    forCount = 0
    cosCount = 0
    sinCount = 0
    tanCount = 0
    endList = []
    while forCount <= forLim:
        forCount = forCount + 1
        curNum = forCount * 5
        tanNum = degrees(tan(curNum))
        sinNum = degrees(sin(curNum))
        cosNum = degrees(cos(curNum))
        endList.append(tanNum)
        endList.append(sinNum)
        endList.append(cosNum)
        if tanNum >= 100 or tanNum <= -100:
            tanCount = tanCount + 1
        if cosNum < 0:
            cosCount = cosCount + 1
        if sinNum < 0:
            sinCount = sinCount + 1
    #print(tanNum)
    #print(sinNum)
    #print(cosNum)
    endList.append(tanCount)
    endList.append(sinCount)
    endList.append(cosCount)
    endList.append(in1)
    endList.append(in2)
    endTup = tuple(endList)
    return endTup

def formatResults(inTup):
    tanCount = inTup[-5]
    sinCount = inTup[-4]
    cosCount = inTup[-3]
    lowInput = inTup[-2]
    highInput = inTup[-1]
    tupleLen = len(inTup) - 5
    forCount = 0
    degCount = 5
    for i in range(0, tupleLen):
        if forCount == 0:
            print("For " + str(degCount) + " degress, there are " + str(inTup[i]) + " degrees Tangent")
        if forCount == 1:
            print("For " + str(degCount) + " degrees, there are " + str(inTup[i]) + " degrees Sin")
        if forCount == 2:
            print("For " + str(degCount) + " degrees, there are " + str(inTup[i]) + " degrees Cos")
        forCount = int(forCount) + 1
        if forCount == 3:
            forCount = 0
            degCount = degCount + 5


    print("There were " + str(tanCount) + " of infinte numbers of Tangent values.")
    print("There were " + str(sinCount) + " of negative Sin values.")
    print("There were " + str(cosCount) + " of negative Cos values.")

#---------------Main-------------------
inTup = getInput()
flippedTup = flipFlop(inTup)
#print(flippedTup)
trigTup = doTrig(flippedTup)
#print (trigTup)
formatResults(trigTup)