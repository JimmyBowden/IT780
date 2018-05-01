"""
Python 3 -- Anaconda -- Cassiopeia --
riotMenu.py
By Jimmy Bowden

This is the main menu for the riot stat pulls using commands

Modules:


"""


import summonerWinrate, recentGameWinrate, topChampionWinrates, makeChampionList
#----------------------------------------------------------------Variables
apiKey = "RGAPI-16e50a2d-19d8-434c-870d-b34ee49a3f79"#the string at the end as the api key


#----------------------------------------------------------------Functions

#this is the main startup function
def mainMenu():
    loopBolean = False #while not true, loop continues
    mainQuestion = """Greetings Summoner!
    If you're looking for statistics about League of Legends Summoners, you've come to the right place.
    Type any of the following commands to pick the desired statitics:
        R for Recent Game Results
        W for Summoner Winrates
        M to Make a new list of champions
        E to exit """

    errorQuestion = """Your input was not correct. Please try again with any of the following commands:
        R for Recent Game Results
        W for Summoner Winrates
        M to Make a new list of champions
        E to exit """

    reloopQuestion = """Type any of the following commands to pick the desired statitics:
        R for Recent Game Results
        W for Summoner Winrates
        M to Make a new list of champions
        E to exit"""
    userRequest = getUserRequest(mainQuestion).upper()

    #After getting user input run through --- all input is converted to upper case
    while loopBolean != True:
        if userRequest == "R":
            #calls for recentGameWinrate.py
            recentGameWinrate.main(apiKey)
            userRequest = getUserRequest(reloopQuestion)
        elif userRequest =="E":
            loopBolean = True
        elif userRequest =="W":
            #calls for summoner winrates
            summonerWinrate.main(apiKey)
            userRequest = getUserRequest(reloopQuestion)
        elif userRequest =="B":
            #calls for Best Champion winrates
            #summonerWinrate.main(apiKey)
            userRequest = getUserRequest(reloopQuestion)
        elif userRequest == "M":
            #call make new champion list
            makeChampionList.main(apiKey)
            userRequest = getUserRequest(reloopQuestion)
        else:
            userRequest = getUserRequest(errorQuestion)
    #the loop is exited and the menu closes            
    exit()
        

#This is to ask the user for input for which module they want to use.
#Returns either a single character or exit
#Looping is handled by mainMenu()
def getUserRequest(question):

    #ask user for input
    print(question)
    userRequest = input().upper()

    return userRequest

#----------------------------------------------------------------Main
if __name__ == "__main__":
    mainMenu()