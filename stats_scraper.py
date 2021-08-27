import urllib
import requests
from bs4 import BeautifulSoup
import csv
import string

filename = "fighters.csv"
csv_writer = csv.writer(open(filename, 'w'))
csv_writer.writerow(['Name', 'Record', 'Height', 'Weight', 'Reach', 'STANCE', 'DOB', 'SLpM', 'Str.Acc', 'SApM', 'Str.Def', 'TD Avg.', 'TD Acc.', 'TD Def.', 'Sub. Avg'])

count = 0
data = []
alphabet = string.ascii_lowercase
for letter in alphabet:
    print(letter)
    url = "http://ufcstats.com/statistics/fighters?char=" + letter + "&page=all"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    fighterData = []
    fighterurls = []
    for link in soup.find_all('a'):
        if link.get('href'):
            if "fighter-details" in link.get('href'):
                fighterurls.append(link.get('href'))
    fighterurls = list( dict.fromkeys(fighterurls) )
    for i in fighterurls:
        fighterurl = i
        fighterpage = requests.get(fighterurl)
        fightersoup = BeautifulSoup(fighterpage.text, 'html.parser').section

        for fighter in fightersoup.find_all('h2'):
            #'class="b-content__title-highlight"'
            name = fighter.text.replace("   ", "").replace("\n", "")
            print(name)
            #writerow name and record
            fighterData.append(name)
            for info in fightersoup.find_all('li'):
                stats = info.text.replace("\n", "").replace("', '", "").replace("    ", "")
                #writerow instead of appending, separate all the stats
                print(stats)
                fighterData.append(stats)
        fighterData.append("\n")
        #writerow fighterData
        #i need to append the fighterData to something
        data.append(fighterData)
        csv_writer.writerow(fighterData)
        fighterData = []

    #print(fighterData)   
#fighterData.to_csv('fighters.csv')
#gets only one fighter per letter for some reason
#csv_writer.writerows(data)
print(data)
#now put that into a csv file

