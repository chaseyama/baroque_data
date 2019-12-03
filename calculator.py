# -- CALCULATION -- #
topicsCounter = {'Arts': 37, 'Business': 10, 'Computers': 13, 'Games': 8, 'Health': 9, 'Home': 13, 'Recreation': 13, 'Science': 13, 'Society': 11, 'Sports': 16}
prices = {"Arts":0.0017, "Business":0.0022, "Computers":0.0036, "Games":0.0069, "Health":0.0012, "Home":0.0011, "Recreation":0.0012, "Science":0.0015, "Society":0.0013, "Sports":0.0023}
totalCost = 0
for category in prices.keys():
    total = topicsCounter[category] * prices[category]
    print(category+":", total)
    totalCost += total

print(totalCost)
