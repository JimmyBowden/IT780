#Jimmy Bowden
#IT 780
#C7.py
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#---------------------Variables
html = urlopen("http://www.showmeboone.com/sheriff/jailresidents/")
#soup = BeautifulSoup(response.text, "lxml")
bsObj = BeautifulSoup(html, "html.parser")


#---------------------Functions
def parseTable():
    infoTable = bsObj.find("tbody", {"id" : "mrc_main_table"})
    #print(infoTable)
    rows = infoTable.findAll("tr")
    rowList = []
    #print(rows[0])
    for item in rows:
        rowString = ""
        for cell in item.findAll("td"):
            rowString = rowString + cell.text.strip() + ","
        rowString = rowString[:-1]
        rowList.append(rowString)
    with open("C7Output.csv", 'wb') as file:
        writer = csv.writer(file, lineterminator='\n')
        #writer.writerows(rowList)
        for item in rowList:
            writer.writerow([item])
    #for line in rows:
        #print(line.text.strip())



#---------------------Main
parseTable()
