import json
from pprint import pprint

with open('jsonme1.json') as data_file:
    data = json.load(data_file)
pprint(data)
