import pandas as pd
from collections import Counter
import json
import os

JSON_PATH = os.getcwd() + "/pretty_outfile.json"

def loadJSON():
    with open(JSON_PATH, "r") as f:
        json_object = json.load(f)
    return json_object

json_object = loadJSON()
docs = json_object['data']

print(len(docs))
# print()
# print(docs[-1])

numClassified = 0
classes = Counter()

for doc in docs:
    cls = doc.get("link_flair_text")
    if cls:
        classes[cls] += 1

for k, v in classes.items():
    print('{0: <40} {1: >20}'.format(k, v))

