import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

countries = []

for country in soup.select(".country")[:20]:

    name = country.select_one(".country-name").text.strip()
    capital = country.select_one(".country-capital").text.strip()
    population = int(country.select_one(".country-population").text.strip())
    area = float(country.select_one(".country-area").text.strip())

    countries.append({
        "name": name,
        "capital": capital,
        "population": population,
        "area": area
    })

print(countries)

from db_manager import CountryDatabaseManager

db = CountryDatabaseManager()

for country in countries:
    db.insert_country(country)

print("20 countries inserted successfully")

print(db.get_all_countries())
