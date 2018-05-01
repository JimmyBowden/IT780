#makeChampionCSV.py
#Jimmy Bowden
#This is to make a csv of champion id and champion name

import requests, csv, time





def main(apiKey):
    #get list of champions only with ids no names
    jsonChampIDList = getChampionList(apiKey)
    #print(jsonChampIDList)
    #make list of ids only
    championIDList = []
    counter = 0
    champDict = jsonChampIDList['data']
    #print(champDict)
    for championID in champDict:
        finalChampID = championID
        #print(finalChampID)
        champName = champDict[str(finalChampID)]['name']
        #print(champName)
        championIDList.append({int(finalChampID): champName})
    #print(championIDList)

    finalDict = {}
    #print("This will take a few minutes")
    #for champID in championIDList:
     #   time.sleep(10)
      #  champ = getChampion(champID, apiKey)
     #   champName = champ['name']
      #  print(champName)
     #   finalDict[champName] = championID
    with open("championList.txt", 'w+') as f:
        f.write(str(championIDList))
        f.close()






def getChampion(champID, apiKey):
    URL = "https://euw1.api.riotgames.com/lol/static-data/v3/champions/" + str(champID) + "?locale=en_US&api_key=" + apiKey
    response = requests.get(URL)
    print(response.json())
    return response.json()

def getChampionList(apiKey):
    URL = "https://eun1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=true&api_key=" + apiKey
    #URL = "https://na1.api.riotgames.com/lol/platform/v3/champions?freeToPlay=false&api_key=" + apiKey
    response = requests.get(URL)
    #print(response.json())
    return response.json()





if __name__ == "__main__":
    #apiKey = "RGAPI-16e50a2d-19d8-434c-870d-b34ee49a3f79"#the string at the end as the api key
    main(apiKey)
