from bs4 import BeautifulSoup
import requests
url = 'https://xeno-canto.org'
response = requests.get(url)
print(response.text)
soup = BeautifulSoup(response.content, "html.parser")