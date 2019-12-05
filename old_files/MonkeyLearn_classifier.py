from monkeylearn import MonkeyLearn
import csv

# MonkeyLearn initialization
topic_ml_id = 'b72b1985a33c279688d4a0f4e5255e4c1e7560be'
events_ml_id = '0923e341f615fbcf8937c9da30800bf0f6a2c5d2'
#events_ml_id = 'b72b1985a33c279688d4a0f4e5255e4c1e7560be' # amanda's
topic_model_id = 'cl_o46qggZq'
events_model_id = 'cl_4omNGduL'

ml = MonkeyLearn(events_ml_id)

# Counter
labels = {}

detail = ml.classifiers.detail(events_model_id).body
# make dictionary of categories
for id in detail['model']['tags']:
    labels[id['name']] = 0


def categorize(filename):
    # get data
    with open('william_SocialMediaData/'+filename,'r') as f: #twitter_impressions.csv
        reader = csv.reader(f)
        data = list(reader)[0]

    result = ml.classifiers.classify(events_model_id, data)

    # print out categories
    for entry in range(len(result.body)):
        id = result.body[entry]['classifications'][0]['tag_name']
        labels[id] += 1

        #print(result.body[entry]['text'] + ':', result.body[entry]['classifications'][0]['tag_name'])


#categorize("twitter_impressions.csv")
#categorize("facebook_ads.csv")
categorize("facebook_advertisers.csv")




# print out list of labels
print(labels)
