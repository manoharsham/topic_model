# topic_model
#How to generate the json file . The json.dumps is used here
python3 WikiExtractor3.py Wikipedia-MachineLearning.xml --sections --lists --json -o MLfiles
#Example code to retreive the json file 

import json
data = [json.loads(line) for line in open('wiki_01', 'r')]
print(data[2]['text'])
print(data[2]['related'])

