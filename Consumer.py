__author__ = 'Ilyas'

import pprint
import requests
import json

data = requests.get('http://127.0.0.1:5000/if/api/v1.0/profile?genderPred=0')
pprint.pprint(json.loads(data.text))

