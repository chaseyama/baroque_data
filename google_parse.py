import json
from urllib.parse import urlparse
import nltk

file = open("SocialMediaData/google_MyActivity.json", "r")
ad_list = json.load(file)

parsed_results = []

for i in range(3,6):
    if "Visited" in ad_list[i]["title"]:
        parsed_results.append(urlparse(ad_list[i]["title"][8:]))
        # print('\n\n', i)
        # print(urlparse(ad_list[i]["title"][8:]))

# Tokenize: http://jeffreyfossett.com/2014/04/25/tokenizing-raw-text-in-python.html

pattern = '\w|\s|/|-|_'

elements = ['netloc','path','param','query','fragment']
parsed_elements = {'netloc': [],
                   'path': [],
                   'param': [],
                   'query': [],
                   'fragment': []}

#for result in parsed_results:
#    for element in elements:
#        print(nltk.regexp_tokenize(result[element], pattern))

#mytweet = "@john lol that was #awesome :)"
print(nltk.regexp_tokenize("http://jeffreyfossett.com/2014/04/25/tokenizing-raw-text-in-python.html", pattern=pattern))
