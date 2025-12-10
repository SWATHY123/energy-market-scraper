import requests
import csv

url = "https://api.opennem.org.au/stats/price/au/nem"

data = requests.get(url).json()
prices = data["data"]["price"]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Price"])
    for p in prices:
        writer.writerow([p])

print("Saved to data.csv")
