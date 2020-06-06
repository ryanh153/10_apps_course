import requests
from bs4 import BeautifulSoup
import pandas


base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
r = requests.get(base_url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, 'html.parser')

max_page_num = int(soup.find_all('a', {'class': 'Page'})[-1].text)
res_per_page = 10

property_list = []
for page in range(0, max_page_num*res_per_page, res_per_page):
    url = f"{base_url}t=0&s={page}.html"
    r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    property_rows = soup.find_all('div', {'class': 'propertyRow'})
    for prop in property_rows:
        d = {}
        d["Price"] = prop.find('h4', {'class': 'propPrice'}).text.strip()

        d["Address"] = prop.find_all('span', {'class': 'propAddressCollapse'})[0].text.strip()
        d['Locality'] = prop.find_all('span', {'class': 'propAddressCollapse'})[1].text.strip()

        try:
            baths = prop.find('span', {'class': 'infoValueFullBath'}).text.strip()
        except AttributeError:
            baths = "0 Full Baths"
        d['Full Baths'] = baths

        try:
            h_baths = prop.find('span', {'class': 'infoValueHalfBath'}).text.strip()
        except AttributeError:
            h_baths = "0 Half Baths"
        d['Half Baths'] = h_baths

        try:
            beds = prop.find('span', {'class': 'infoBed'}).text.strip()
        except AttributeError:
            beds = "0 Beds"
        d['Beds'] = beds

        try:
            sq_ft = prop.find('span', {'class': 'infoSqFt'}).text.strip()
        except AttributeError:
            sq_ft = "No Square Footage Data"
        d['SqFt'] = sq_ft

        for col_grp in prop.find_all('div', {'class': 'columnGroup'}):
            for f_grp, f_name in zip(col_grp.find_all('span', {'class': 'featureGroup'}), col_grp.find_all('span', {'class', 'featureName'})):
                if "Lot Size" in f_grp.text:
                    d['Lot Size'] = f_grp.text.strip() + ' ' + f_name.text.strip()
                    break

        property_list.append(d)

df = pandas.DataFrame(property_list)
df.to_csv('output_csv.csv')