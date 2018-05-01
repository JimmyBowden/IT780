"""
Python 3 -- Anaconda --  --
summonerWinrate.py
By Jimmy Bowden

This is the  winrate modules. This pulls winrates for a user in NA
"""
import requests
import matplotlib.pyplot as plt


#---------------------------------------------------Variables
champNum = 10
introText = "Welcome to the Ranked Queue winrates. This will the winrates for a specified summoner and queue\nPlease enter a Summoner name:\n"
secondText = "Choose a ranked queue by entering one of the following:\ns for Solo Queue\nf for 5's Flex Queue\nt for 3's Flex Queue\n"

chartTitleList = ["Ranked 5's Flex Queue", "Ranked 3's Flex Queue", "Ranked Solo Queue"]



#---------------------------------------------------functions

def getTopWinrates(apiKey):
    print("")
    #Enter the loop to get winrates 
    #try:
    queueFlag = False
    summonerFlag = False

    #choose the summoner name
    while summonerFlag ==False: 
        inputSummoner = input(introText)
        if inputSummoner == "":
            print("Please enter a summoner name.")
        else:
            replacedInputSummoner = inputSummoner.replace(" ", "%20")
            summonerFlag = True
    
    #Choose the queue with a one char input
    while queueFlag == False:
        inputQueue = input(secondText).upper()
        if inputQueue == "S":
            queueNumber = 2
            queueFlag = True
        elif inputQueue =="F":
            queueNumber = 0
            queueFlag = True
        elif inputQueue == "T":
            queueNumber = 1
            queueFlag = True
        else:
            print(str(inputQueue) + " is not a correct input. Please try again.")

    #testSummoner = "Too%20Legitness"
    
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


    #make the pie chart of win rates for a queue
    fig1, ax1 = plt.subplots()

    sizes = [wins, losses]
    chartLables = ["Wins (" + str(wins) + ")", "Losses (" + str(losses) + ")"]

    ax1.pie(sizes, labels=chartLables, autopct='%1.1f%%', explode=[0.1, 0], shadow=True, startangle=90) #wins first in each thing
    ax1.axis('equal') #equal aspect ratio to make this a circle
    plt.title(inputSummoner + "'s " + chartTitleList[queueNumber] + " Win-Lose")
    plt.show()
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
    main(apiKey)
    