from fastapi import FastAPI
from db_manager import CountryDatabaseManager
from pydantic import BaseModel

app = FastAPI()

db = CountryDatabaseManager()

class Country(BaseModel):
    name: str
    capital: str
    population: int
    area: float

@app.get("/countries")
def get_all_countries():

    countries = db.get_all_countries()

    result = []

    for country in countries:
        result.append({
            "name": country[0],
            "capital": country[1],
            "population": country[2],
            "area": country[3]
        })

    return result

@app.get("/countries/{country_name}")
def get_country(country_name):

    country = db.get_country(country_name)

    if country:
        return {
            "name": country[0],
            "capital": country[1],
            "population": country[2],
            "area": country[3]
        }

    return {"message": "Country not found"}

@app.post("/countries")
def create_country(country: Country):

    db.insert_country(country.dict())

    return {"message": "Country added successfully"}

@app.put("/countries/{country_name}")
def update_country(country_name: str, country: Country):

    db.update_country(
        country_name,
        country.capital,
        country.population,
        country.area
    )

    return {"message": "Country updated successfully"}

@app.delete("/countries/{country_name}")
def delete_country(country_name):

    db.delete_country(country_name)

    return {"message": "Country deleted successfully"}