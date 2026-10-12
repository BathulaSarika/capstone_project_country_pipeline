import requests
import pandas as pd

url = "http://127.0.0.1:8000/countries"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(df)

df.to_csv("exported_countries.csv", index=False)

print("CSV exported successfully")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.scatter(
    df["population"],
    df["area"]
)

plt.title("Population vs Area")

plt.xlabel("Population")

plt.ylabel("Area (sq km)")

plt.grid(True)

plt.savefig("population_vs_area.png")

plt.show()