''' Q. Use the BeautifulSoup and requests Python packages to print out a list of all 
the article titles on the New York Times homepage.'''

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find article headlines
for heading in soup.find_all(["h2", "h3"]):
    text = heading.get_text(" ", strip=True)

    if text:
        print(text)