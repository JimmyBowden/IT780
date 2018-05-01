"""
Python 3 -- Anaconda --  --
recentGameWinrate.py
By Jimmy Bowden

This is the  winrate modules. This pulls winrates for a user in NA
"""
import requests
import matplotlib.pyplot as plt
import time
import numpy as np
#---------------------------------------------------Variables

introText = "Welcome to the Recent Game Winrate module. This will show you a summoner's winrate for the recent games played.\nPlease enter a Summoner name:\n"


chartTitleList = ["Ranked 5's Flex Queue", "Ranked 3's Flex Queue", "Ranked Solo Queue"]



#---------------------------------------------------functions

def getTopWinrates(apiKey):
    print("")
    #Enter the loop to get winrates 
    #try:
    summonerFlag = False

    #choose the summoner name
    while summonerFlag ==False: 
        inputSummoner = input(introText)
        if inputSummoner == "":
            print("Please enter a summoner name.")
        else:
            replacedInputSummoner = inputSummoner.replace(" ", "%20")
            summonerFlag = True
    

    #testSummoner = "Too%20Legitness"
    
    #get summoner info from summoner name
    summonerInfo = getSummonerByName(replacedInputSummoner, apiKey)
    # get summoner id from info
    accountID = str(summonerInfo["accountId"])
    summonerID = str(summonerInfo["id"])
    #print(accountID)
    #get dict of all matches a player has played this season
    recentMatches = getSummonerRecentMatches(accountID, apiKey)
    
    #Parse through list of recent matches and get count of wins and loses
    matchCount = 0
    winCount = 0
    loseCount = 0
    topW = 0
    topL = 0
    midW = 0
    midL = 0
    jungleW = 0
    jungleL = 0
    botW = 0
    botL = 0
    inGameSummonerID = 0
    print("Processing, may take up to 20 seconds...")
    for match in recentMatches["matches"]:
        gameID = match["gameId"]
        #print(gameID)
        time.sleep(.1)
        currentMatch = getMatch(gameID, accountID, apiKey)
        #print(currentMatch)
        gamePlayerInfo = currentMatch['participantIdentities'] #this is a list of nested dictionaries
        gameParticipants = currentMatch['participants']
        playerCount = 0
        #print(gamePlayerInfo)
        for players in gamePlayerInfo:   #players is a dictionary with more nested in it
            #print(players["player"]["accountId"])
            #print(players["participantId"])
            if players["player"]["accountId"] == int(accountID):
                partID = (players['participantId'])
                #print(partID)
                matchResult = gameParticipants[partID-1]['stats']['win']
                laneResult = gameParticipants[partID-1]['timeline']['lane']
            #print(test)
                if matchResult == True:
                    winCount += 1
                    if laneResult == "TOP":
                        topW += 1
                    elif laneResult == "JUNGLE":
                        jungleW += 1
                    elif laneResult == "MIDDLE":
                        midW += 1
                    elif laneResult == "BOTTOM":
                        botW += 1
                else:
                    loseCount = loseCount + 1
                    if laneResult == "TOP":
                        topL += 1
                    elif laneResult == "JUNGLE":
                        jungleL += 1
                    elif laneResult == "MIDDLE":
                        midL += 1
                    elif laneResult == "BOTTOM":
                        botL += 1
                break
        if matchCount == 19:
            break
        matchCount = matchCount + 1
    print(inputSummoner + " got " + str(winCount) + " wins and " + str(loseCount) + " losses in your last 20 matches!")
    #print(midW)
    #print(midL)
    winList = [topW, jungleW, midW, botW]
    loseList = [topL, jungleL, midL, botL]
    #make the bars for the chart
    
    chartLables = ["Top", "Jungle", "Middle", "Bottom"]
    width = 0.35
    ind = np.arange(3) #x locations for groups

    p1 = plt.bar((1, 2, 3, 4), winList, width, color='blue')
    p2 = plt.bar((1, 2, 3, 4), loseList, width, bottom = winList, color='red')

    plt.ylabel("Number of Matches")
    plt.xlabel("Lanes")
    plt.title("Wins/Losses per Lane")

    plt.xticks((1,2,3,4), chartLables)
    
    plt.legend((p1[0], p2[0]), ("Wins", "Losses"))
    plt.show()
    #ax1.pie(sizes, labels=chartLables, autopct='%1.1f%%', explode=[0.1, 0], shadow=True, startangle=90) #wins first in each thing
    #ax1.axis('equal') #equal aspect ratio to make this a circle
    #plt.title(inputSummoner + "'s " + chartTitleList[queueNumber] + " Win-Lose")
        #plt.show()
    #except:
        #pass



def getSummonerByName(summonerName, apiKey):
    URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + apiKey
    response = requests.get(URL)
    #print(URL)

    return response.json() #returns dict of summoner info

def getSummonerRecentMatches(accountID, apiKey):
    URL = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(accountID) + "?api_key=" + apiKey
    #URL = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/35704404?api_key=RGAPI-5aa59b8f-fa65-4ff1-8c35-1daa5fb32422"
    response = requests.get(URL)
    #print(URL)
    #print(response.json())

    return response.json()

def getMatch(gameID, accountID, apikey):
    URL = "https://na1.api.riotgames.com/lol/match/v3/matches/" + str(gameID) + "?api_key=" + apikey
    response = requests.get(URL)
    #print(URL)

    return response.json()




#---------------------------------------------------main
def main(apiKey):
    getTopWinrates(apiKey)






if __name__ == "__main__":
    #apiKey = "RGAPI-5aa59b8f-fa65-4ff1-8c35-1daa5fb32422"#the string at the end as the api key
    main(apiKey)
    