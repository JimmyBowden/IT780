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
outputFile = 'C7Output.csv'


#---------------------Functions
def parseTable():
    infoTable = bsObj.find("tbody", {"id" : "mrc_main_table"})
    rows = infoTable.findAll("tr")
    rowList = []
    for item in rows:
        rowTuple = ()
        rowString = ""
        for cell in item.findAll("td"):
            rowString = rowString + cell.text.strip() + ","
        rowString = rowString[:-1]
        rowString = rowString + "\n"
        rowList.append(rowString)
    with open(outputFile, 'w', encoding="utf-8") as output:
        writer = csv.writer(output, dialect='excel', delimiter=",")
        for row in rowList:
            cellsList = tuple(filter(None, row.split(',')))
            writer.writerow(cellsList)
    #for line in rows:
        #print(line.text.strip())



#---------------------Main
parseTable()
