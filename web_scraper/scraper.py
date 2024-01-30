import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_San_Diego"

def get_citations_needed_report(url):
    response = requests.get(url)
    markup = response.text
    
    soup = BeautifulSoup(markup, 'html.parser')
    citation_needed = soup.select('a[title="Wikipedia:Citation needed"]')
    
    citation_count = get_citations_needed_count(url)
    
    citation_output = f"Citation needed for the following {citation_count} passage(s):\n\n"

    for link in citation_needed:
        grandparent = link.find_parent('p')  # Find the parent <p> tag
        if grandparent:
            citation_output += grandparent.get_text() + "\n"
    return citation_output

def get_citations_needed_count(url):
    response = requests.get(url)
    markup = response.text
    
    soup = BeautifulSoup(markup, 'html.parser')
    citation_needed = soup.select('a[title="Wikipedia:Citation needed"]')
    
    count = 0
    
    for link in citation_needed:
        count += 1
    return count

print(get_citations_needed_report(url))
print(get_citations_needed_count(url))