from lxml import html
import requests
import csv

# -- CLASSIFICATION -- #

will_readkey = "yC4MZuxlY9oH"
amanda_readkey = "6g5EAAJWv5HO"
url = "https://api.uclassify.com/v1/uclassify/topics/classify?readkey="+amanda_readkey+"&text="
topicsCounter = {"Arts":0,"Business":0,"Computers":0,"Games":0,"Health":0,"Home":0,"Recreation":0,"Science":0,"Society":0,"Sports":0}
csvUrls =  ["https://raw.githubusercontent.com/chaseyama/baroque_data/master/william_SocialMediaData/csv-facebook_ads.csv",
            "https://raw.githubusercontent.com/chaseyama/baroque_data/master/william_SocialMediaData/csv-facebook_advertisers.csv",
            "https://raw.githubusercontent.com/chaseyama/baroque_data/master/william_SocialMediaData/csv-twitter_engagements.csv",
            "https://raw.githubusercontent.com/chaseyama/baroque_data/master/william_SocialMediaData/csv-twitter_impressions.csv"]

for i, csvUrl in enumerate(csvUrls):
    print('requesting page...')
    csvPage = requests.get(csvUrl)
    csvList = html.fromstring(csvPage.content).text
    keywords = csvList.split(',')
    print("keywords for", csvUrl[85:], ":", keywords[:5])


    # with open(csvUrl, 'r') as f:
    #     reader = csv.reader(f)
    #     keywords = list(reader)

    for keyword in keywords:
        page = requests.get(url + keyword.replace(" ", "+"))
        tree = html.fromstring(page.content)
        string = tree.text
        exec('weights = ' + string)
        topicsCounter[max(weights, key=weights.get)] += 1

print(topicsCounter)
