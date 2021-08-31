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
            name = fighter.text.replace("   ", "").replace("\n", "").replace("Record:", ",").strip()
            print(name)
            nameAndRecord = name.split(",")
            nameAndRecord[0] = nameAndRecord[0].strip()
            nameAndRecord[1] = nameAndRecord[1].strip()

            fighterData.append(nameAndRecord[0])
            fighterData.append(nameAndRecord[1])
            for info in fightersoup.find_all('li'):

                stats = info.text.replace("\n", "").replace("', '", "").replace("    ", "")
                stats = stats.replace("Height:", "")
                stats = stats.replace("Weight:", "")
                stats = stats.replace("Reach:", "")
                stats = stats.replace("STANCE:", "")
                stats = stats.replace("DOB:", "")
                stats = stats.replace("SLpM:", "")
                stats = stats.replace("Str. Acc.:", "")
                stats = stats.replace("SApM:", "")
                stats = stats.replace("Str. Def:", "")
                stats = stats.replace("TD Avg.:", "")
                stats = stats.replace("TD Acc.:", "")
                stats = stats.replace("TD Def.:", "")
                stats = stats.replace("Sub. Avg.:", "")
                
                print(stats)
                fighterData.append(stats)
        fighterData = list(filter(None, fighterData))
        data.append(fighterData)
        csv_writer.writerow(fighterData)
        fighterData = []

print(data)


