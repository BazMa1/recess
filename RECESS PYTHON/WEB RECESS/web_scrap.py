from bs4 import BeautifulSoup
import requests
url = 'https://xeno-canto.org'
response = requests.get(url)
print(response.text)
soup = BeautifulSoup(response.content, "html.parser")

#results = soup.find(id="ResultsContainer")
#titles = soup.find_all('div', attrs={'class', 'taxon-list-item'})
#titles_list = []

#get title of the website
#soup = BeautifulSoup(response.content,'html.parser')
#title = soup.find('title')
#print (title)
import pandas as pd
import json
import csv
import requests
from bs4 import BeautifulSoup
# Make a GET request to the website
response = requests.get('https://xeno-canto.org')
#response = requests.get('https://www.worldbirdnames.org')
# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')
# Find all the elements on the page that have the `class` attribute `taxon-list-item`
taxon_list_items = soup.find_all('div', class_='taxon-list-item')
# Create a list to store the bird species data
bird_species_data = []
# Iterate over the `taxon-list-item` elements
for taxon_list_item in taxon_list_items:
    # Get the bird species name
    bird_species_name = taxon_list_item.find('a', class_='taxon-list-item-name').text
    # Get the bird family
    bird_family = taxon_list_item.find('span', class_='taxon-list-item-family').text
    # Get the bird order
    bird_order = taxon_list_item.find('span', class_='taxon-list-item-order').text
    # Add the bird species data to the list
    bird_species_data.append({
        'bird_species_name': bird_species_name,
        'bird_family': bird_family,
        'bird_order': bird_order
    })
# Save the bird species data to a CSV file
with open('bird_species_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(bird_species_data)
# Save the bird species data to a JSON file
with open('bird_species_data.json', 'w') as f:
    json.dump(bird_species_data, f)


#extract songs
df = pd.read_html(response.content)
df.to_csv("songs.csv")


# Get the data from the response
data = response.json()

# Print the data
print(data)


#extract songs from website 
if response.status_code == 200:
    data = response.json()
# Create a list to store the songs
    if "recordings" in data:
        bird_songs = list({recording["sp"] for recording in data["recordings"]})
        print(bird_songs)
else:
    print("Error: Unable to fetch data from the API.")



