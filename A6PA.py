#A6PA.py   (Part A)
#Jimmy Bowden
#IT780


import C8b
import C4
import matplotlib.pyplot as plt

#------------------------------------------------Variables



#------------------------------------------------Functions




#------------------------------------------------Main
dictList = C4.readNameCSV()
myDict = C4.readRatingCSV(dictList)
myInput = input("Enter a name: ").capitalize()
pearNeighbor = C8b.computeNearestNeighbor(myInput, myDict, 1, True)
pearRecommened = C8b.recommend(myInput, myDict, 1, True)
print("Pearson:")
print("Nearest Neighhbors: ", pearTest1)
print("Recommendations: ", pearTest2)
print("")
