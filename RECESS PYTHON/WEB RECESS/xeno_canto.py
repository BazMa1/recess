from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import csv
from bs4 import BeautifulSoup
url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        bird_species = list({recording["sp"] for recording in data["recordings"]})

        # Specify the file path for the CSV file
        csv_file_path = "bird_species.csv"

        # save the species_list to the CSV file
        with open(bird_species.csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["bird_species"])  # Write header row
            writer.writerows([[species] for species in bird_species])  # Write species names row by row

        print("Data saved to CSV file successfully.")
else:
    print("Error: Unable to fetch data from the API.")
#print('please modify this to so that you be creative enough to do more with the API https://xeno-canto.org/explore/api \nbecause the trick is on playing around with the query parameters')
# Save the bird species data to a JSON file
with open('bird_species.json', 'w') as f:
    json.dump(bird_species, f)
