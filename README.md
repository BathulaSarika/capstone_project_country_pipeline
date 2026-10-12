End-to-End Country Data Pipeline & Analytics System
Features
Scrape first 20 countries from Scrapethissite
SQLite database with Country Name as Primary Key
OOP CRUD operations
FastAPI REST API
CSV export
Scatter plot visualization
Files
scraper.py
db_manager.py
api.py
client.py
countries.db
exported_countries.csv
population_vs_area.png
Run
pip install -r requirements.txt

python scraper.py

uvicorn api:app --reload

python client.py
