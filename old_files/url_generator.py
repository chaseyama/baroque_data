import csv

def get_urls(filename): # creates csv of urls
    # get data
    with open('william_SocialMediaData/'+filename,'r') as f: #twitter_impressions.csv
        reader = csv.reader(f)
        data = list(reader)[0]

    urls = []

    for interest in data:
        url = "https://api.uclassify.com/v1/uclassify/topics/classify?readkey=yC4MZuxlY9oH&text="
        str = interest.replace(" ", "+")
        url += str

        urls.append(url)

    with open('url_outputs/' + 'url_' + filename[4:-4] + '.csv', mode='w') as output:
        writer = csv.writer(output, delimiter=',')

        writer.writerow(urls)



get_urls("csv-twitter_impressions.csv") # twitter impressions
get_urls("csv-twitter_engagements.csv") # twitter engagements
get_urls("csv-facebook_ads.csv") # facebook ad interests
get_urls("csv-facebook_advertisers.csv") # facebook ad companies
