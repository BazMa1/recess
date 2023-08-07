import pandas as pd
import json
import csv
import requests
from bs4 import BeautifulSoup
url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
if response.status_code == 200:
    data = response.json()
# Create a list to store the bird species data
    if "recordings" in data:
        bird_species = list({recording["sp"] for recording in data["recordings"]})
        print(bird_species)
else:
    print("Error: Unable to fetch data from the API.")

print("save species to csv")
if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        species_list = list({recording["sp"] for recording in data["recordings"]})

        # Specify the file path for the CSV file
        csv_file_path = "bird_species.csv"

        # Write the species_list to the CSV file
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
# Write TITLE row
            writer.writerow(["BIRD SPECIES"])  # Write header row
            writer.writerows([[species] for species in bird_species])  # Write species names row by row

        print("Data saved to CSV file successfully.")
else:
    print("Error: failed to fetch data from the API.")
    
    
# Save the bird species data to a JSON file
with open('bird_species.json', 'w') as f:
    json.dump(bird_species, f)


#extract songs from website 
if response.status_code == 200:
    data = response.json()
# Create a list to store the songs
    if "recordings" in data:
        bird_songs = list({recording["en"] for recording in data["recordings"]})
        print(bird_songs)
else:
    print("Error: Unable to fetch data from the API.")
print('==EXTRACTED SONGS==')
#extract songs
    
if response.status_code == 200:
    data = response.json()
# Create a list to store the songs
    if "recordings" in data:
        bird_songs = list({recording["sp"] for recording in data["recordings"]})
        print(bird_songs)
else:
    print("Error: Unable to fetch data from the API.")


# Make a request to the API endpoint
#response = requests.get("http://xeno-canto.org/api/2/recordings")
# Parse the JSON response
#Data = response.json()
# Print the data
#print(data)