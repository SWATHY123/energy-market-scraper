import matplotlib.pyplot as plt
import csv

prices = []

with open("data.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        prices.append(float(row[0]))

plt.plot(prices)
plt.title("Electricity Prices")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()
