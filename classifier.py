from monkeylearn import MonkeyLearn
import csv

# get data
#data = ['animation','computer news','space and astronomy', 'music news and general info']
with open('william_SocialMediaData/twitter_impressions.csv','r') as f:
    reader = csv.reader(f)
    data = list(reader)[0]

#print(data)

#ml_id = 'b72b1985a33c279688d4a0f4e5255e4c1e7560be'
ml_id = '0923e341f615fbcf8937c9da30800bf0f6a2c5d2'
ml = MonkeyLearn(ml_id)
#model_id = 'cl_o46qggZq'
model_id = 'cl_4omNGduL'
result = ml.classifiers.classify(model_id, data)

for entry in range(len(result.body)):
    #print(result.body[entry])
    #print('\n\n')
    print(result.body[entry]['text'] + ':', result.body[entry]['classifications'][0]['tag_name'])
