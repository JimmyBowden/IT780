"""
Python 3 -- Anaconda -- Cassiopeia --
topChampionWinrates.py
By Jimmy Bowden

This is the Top champions winrate modules. This pulls the top x champions for a user in NA
"""

import requests
import matplotlib


#---------------------------------------------------Variables
champNum = 10
introText = "Welcome to the top Champion winrates. This will show you your top " + str(champNum) + " champions by winrates.\nPlease enter your Summoner name:\n"
secondText = "Enter in a champion name:\n"
apiKey = "RGAPI-5aa59b8f-fa65-4ff1-8c35-1daa5fb32422"#the string at the end as the api key



#---------------------------------------------------functions

def getTopWinrates(apiKey):
    print("")
    #Enter the loop to get winrates 
   # try:
    championFlag = False
    summonerFlag = False

    #choose the summoner name
    while summonerFlag ==False: 
        inputSummoner = input(introText)
        if inputSummoner == "":
            print("Please enter a summoner name.")
        else:
            replacedInputSummoner = inputSummoner.replace(" ", "%20")
            summonerFlag = True
    #Get champion list from csv


    
    #Choose the champion
    while championFlag == False:
        inputChampion = input(secondText).upper()
        if inputChampion in champList:
            
            championFlag = True
        else:
            print(str(inputQueue) + " is not a correct input. Please try again.")

    #get summoner info from summoner name
    summonerInfo = getSummonerByName(replacedInputSummoner, apiKey)
    # get summoner id from info
    summonerID = summonerInfo["id"]


    #get ranked info for each ranked que from summoner id
    summonerRankedInfo = getSummonerWinRate(summonerID, apiKey)
    #get dict of ranked info
    rankedDict = summonerRankedInfo[queueNumber] # 0 = flex 1 = 3's 2 = solo
    wins = rankedDict["wins"]
    losses = rankedDict["losses"]
    winLoseRatio = wins / (losses + wins)
    print(inputSummoner + " has " + str(wins) + " wins and " + str(losses) + " losses!")
    print(inputSummoner + " has a win-lose ratio of " + str(winLoseRatio))
    #except:
        #pass





def getSummonerByName(summonerName, apiKey):
    URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + apiKey
    response = requests.get(URL)
    #print(URL)

    return response.json() #returns dict of summoner info

def getSummonerWinRate(summonerID, apiKey):
    URL = "https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/" + str(summonerID) + "?api_key=" + apiKey
    response = requests.get(URL)
    #print(URL)

    return response.json() #returns nested dict of ranked info


#---------------------------------------------------main
def main(apiKey):
    getTopWinrates(apiKey)






if __name__ == "__main__":
    #riotapi.set_region("NA")
    #Currently has to be set every 24 hours
    #riotapi.set_api_key("RGAPI-0a8e6ab1-44e6-4209-a075-0b475f6e587f")
    main(apiKey)
    