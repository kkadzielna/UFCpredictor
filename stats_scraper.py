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

    fighterurl = []
    for link in soup.find_all('a'):
        if link.get('href'):
            if "fighter-details" in link.get('href'):
                fighterurl.append(link.get('href'))
    fighterurl = list( dict.fromkeys(fighterurl) )
    print(fighterurl)

