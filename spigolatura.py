import requests

url = "https://www.focus.it/cultura/curiosita/qual-e-il-primo-blackout-della-storia"
response = requests.get(url)
html = response.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

# Trova il primo <h1>
titolo = soup.find("h1").text
print(titolo)

# Trova tutti i paragrafi <p>
paragrafi = soup.find_all("p")
for p in paragrafi:
    print(p.text)

#Stampa tutto il contenuto
print(soup.prettify())
