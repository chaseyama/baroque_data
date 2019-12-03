# -- CALCULATION -- #
#topicsCounter = {'Arts': 37, 'Business': 10, 'Computers': 13, 'Games': 8, 'Health': 9, 'Home': 13, 'Recreation': 13, 'Science': 13, 'Society': 11, 'Sports': 16}
topicsCounter = {'Arts': 71, 'Business': 38, 'Computers': 26, 'Games': 11, 'Health': 24, 'Home': 33, 'Recreation': 70, 'Science': 21, 'Society': 34, 'Sports': 32}
prices = {"Arts":0.0017, "Business":0.0022, "Computers":0.0036, "Games":0.0069, "Health":0.0012, "Home":0.0011, "Recreation":0.0012, "Science":0.0015, "Society":0.0013, "Sports":0.0023}

for category in prices.keys():
    prices[category] = round(topicsCounter[category] * prices[category], 5)
    #print(category+":", round(total, 5))

totalCost = 0
for price in prices.values():
    totalCost += price

print(prices)
print("total price:", totalCost)

totalCount = 0
for count in topicsCounter.values():
    totalCount += count

print("total keyword count:", totalCount)
