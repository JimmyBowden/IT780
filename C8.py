#Jimmy Bowden
#C8.py

from math import sqrt
import C4

class myRecommender:
    def __init__(self):
        from math import sqrt

    def manhattan(rating1, rating2):
        """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
        """
        distance = 0
        commonRatings = False 
        for key in rating1:
            if key in rating2:
                distance += abs(rating1[key] - rating2[key])
                commonRatings = True
        if commonRatings:
            return distance
        else:
            return -1 #Indicates no ratings in common


    def minkowski(rating1, rating2, r):
        distance = 0
        commonRatings = False 
        for key in rating1:
            if key in rating2:
                distance += pow((abs(float(rating1[key]) - float(rating2[key]))), r)
                commonRatings = True
        if commonRatings:
            distance = pow(distance,(1/r))
            return distance
        else:
            return -1 #Indicates no ratings in common


    def euclidean(rating1, rating2):
        distance = 0
        commonRatings = False 
        for key in rating1:
            if key in rating2:
                distance += (rating1[key] - rating2[key]) ** 2
                commonRatings = True
        if commonRatings:
            distance = sqrt(distance)
            return distance
        else:
            return -1 #Indicates no ratings in common


    def computeNearestNeighbor(username, users, r, Pearson = False):
        """creates a sorted list of users based on their distance to username"""
        distances = []
        for user in users:
            if user != username:
                if Pearson == True:
                    distance = pearson(users[user], users[username])
                else:
                    distance = minkowski(users[user], users[username], r)

                
                distances.append((distance, user))
        # sort based on distance -- closest first
        distances.sort(reverse=Pearson)
        return distances

    def recommend(username, users, r, Pearson = False):
        """Give list of recommendations"""
        # first find nearest neighbor
        if Pearson == True:
            nearest = computeNearestNeighbor(username, users, r, True)[0][1]
        else:
            nearest = computeNearestNeighbor(username, users, r)[0][1]
        recommendations = []
        # now find bands neighbor rated that user didn't
        neighborRatings = users[nearest]
        userRatings = users[username]
        for artist in neighborRatings:
            if not artist in userRatings:
                recommendations.append((artist, neighborRatings[artist]))
        # using the fn sorted for variety - sort is more efficient
        return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)


    def pearson(rating1, rating2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        for key in rating1:
            if key in rating2:
                n += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        if n == 0:
            return 0
        # now compute denominator
        denominator = (sqrt(sum_x2 - pow(sum_x, 2) / n)
                    * sqrt(sum_y2 - pow(sum_y, 2) / n))
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / n) / denominator


    def mainRun():
        dictList = C4.readNameCSV()
        myDict = C4.readRatingCSV(dictList)
        myInput = input("Enter a name: ").capitalize()

        manTest1 = computeNearestNeighbor(myInput, myDict, 1)
        manTest2 = recommend(myInput, myDict, 1)
        print("Manhattan:")
        print("Nearest Neighhbors: ", manTest1)
        print("Recommendations: ", manTest2)
        print("")

        euTest1 = computeNearestNeighbor(myInput, myDict, 2)
        euTest2 = recommend(myInput, myDict, 2)
        print("Eucledian:")
        print("Nearest Neighhbors: ", euTest1)
        print("Recommendations: ", euTest2)
        print("")

        pearTest1 = computeNearestNeighbor(myInput, myDict, 1, True)
        pearTest2 = recommend(myInput, myDict, 1, True)
        print("Pearson:")
        print("Nearest Neighhbors: ", pearTest1)
        print("Recommendations: ", pearTest2)
        print("")
        #-----------------------------Main---------------------------------
    #mainRun()
