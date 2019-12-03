from lxml import html
import requests
import csv

# -- CLASSIFICATION -- #

will_readkey = "yC4MZuxlY9oH"
amanda_readkey = "6g5EAAJWv5HO"
url = "https://api.uclassify.com/v1/uclassify/topics/classify?readkey="+will_readkey+"&text="

csvUrls =  ["https://raw.githubusercontent.com/chaseyama/baroque_data/master/william_SocialMediaData/csv-facebook_ads.csv",
            "https://raw.githubusercontent.com/chaseyama/baroque_data/master/william_SocialMediaData/csv-twitter_engagements.csv",
            "https://raw.githubusercontent.com/chaseyama/baroque_data/master/william_SocialMediaData/csv-twitter_impressions.csv"]

fileSources = ['facebook_ads', 'twitter_engagements', 'twitter_impressions']

for i, csvUrl in enumerate(csvUrls):
    print('requesting page...')
    csvPage = requests.get(csvUrl)
    csvList = html.fromstring(csvPage.content).text
    keywords = csvList.split(',')

    topicsList = {'Arts': [], 'Business': [], 'Computers': [], 'Games': [], 'Health': [], 'Home': [], 'Recreation': [], 'Science': [], 'Society': [], 'Sports': []}

    for keyword in keywords:
        page = requests.get(url + keyword.replace(" ", "+"))
        tree = html.fromstring(page.content)
        string = tree.text
        exec('weights = ' + string)

        category = max(weights, key=weights.get)

        if keyword not in topicsList[category]:
            topicsList[category].append(keyword)

    print(fileSources[i])
    print(topicsList)
