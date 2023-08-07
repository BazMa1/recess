import requests
import csv
import json
from bs4 import BeautifulSoup

url = 'https://xeno-canto.org'
def get_bird_species(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        species_data = []

        # Find all bird species elements on the page
        species_elements = soup.select('.mb-1')
        
        for species_element in species_elements:
            species_name = species_element.find('a').text
            species_info = species_element.find_next('div').text.strip()
            species_data.append({'species': species_name, 'info': species_info})

        return species_data
    else:
        print(f"Failed to fetch data from {url}")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['species', 'info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    url = 'https://xeno-canto.org'
    bird_species_data = get_bird_species(url)

    if bird_species_data:
        # Save to CSV
        csv_filename = 'bird_species.csv'
        save_to_csv(bird_species_data, csv_filename)
        print(f"CSV file '{csv_filename}' generated successfully.")

        # Save to JSON
        json_filename = 'bird_species.json'
        save_to_json(bird_species_data, json_filename)
        print(f"JSON file '{json_filename}' generated successfully.")
