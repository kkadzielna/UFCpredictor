import urllib
import requests
from bs4 import BeautifulSoup
import csv
import string

filename = "fighters.csv"
csv_writer = csv.writer(open(filename, 'w'))

alphabet = string.ascii_lowercase
for letter in alphabet:
    url = "http://ufcstats.com/statistics/fighters?char={letter}&page=all"
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
        fightersoup = BeautifulSoup(fighterpage.text, 'html.parser')
        #so maybe make columns in the csv file and fill them based on the titles of the li blocks?
        """
        for info in fightersoup.find_all('li'):
            #info.get_text().remove('/n')
            fighter = info.text.replace("\n", "").replace("', '", "").replace("    ", "")
            fighterData.append(fighter)
            #fighterData.append(info.contents)
        print(fighterData)
        """
        for fighter in fightersoup.find_all('h2'):
            #info.get_text().remove('/n') 'class="b-content__title-highlight"'
            name = fighter.text.replace("   ", "").replace("\n", "")
            print(name)
            fighterData.append(name)
            for info in fightersoup.find_all('li'):
                stats = info.text.replace("\n", "").replace("', '", "").replace("    ", "")
                print(stats)
                fighterData.append(stats)
        #print(fighterData)        

    #now put that into a csv file

