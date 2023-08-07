#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
url = 'https://xeno-canto.org'
response = requests.get('https://xeno-canto.org')
# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')
#taxon_list_items = soup.find_all('div', class_='taxon-list-item')
#driver = webdriver.Chrome(url)
bird_species = []

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    bird_species=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    bird_species.append(bird_species.text)



