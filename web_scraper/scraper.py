import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_San_Diego"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())