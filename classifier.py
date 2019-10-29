from monkeylearn import MonkeyLearn
import csv

def categorize(filename):
    # get data
    with open('william_SocialMediaData/'+filename,'r') as f: #twitter_impressions.csv
        reader = csv.reader(f)
        data = list(reader)[0]

    topic_ml_id = 'b72b1985a33c279688d4a0f4e5255e4c1e7560be'
    events_ml_id = '0923e341f615fbcf8937c9da30800bf0f6a2c5d2'
    ml = MonkeyLearn(events_ml_id)

    topic_model_id = 'cl_o46qggZq'
    events_model_id = 'cl_4omNGduL'
    result = ml.classifiers.classify(events_model_id, data)

    for entry in range(len(result.body)):
        print(result.body[entry]['text'] + ':', result.body[entry]['classifications'][0]['tag_name'])


categorize("twitter_impressions.csv")
