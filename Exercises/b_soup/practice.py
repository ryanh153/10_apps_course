import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c, 'html.parser')
divs = soup.find_all('div', {'class': 'cities'})
h2s = [div.find_all('h2') for div in divs]
cities = [h2[0].text for h2 in h2s]
print(cities)
