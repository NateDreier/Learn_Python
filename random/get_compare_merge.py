#!/usr/bin/env python3

import requests
import json
#from jq import jq
import jello
import re

#{'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}
#{'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson', 'avatar': 'https://reqres.in/img/faces/8-image.jpg'}

headers = {
    "Content-Type": "application/json",
}
url = "https://reqres.in/api/users?page=2"
r = requests.get(url, headers=headers)
j = r.json()
#first = jq(".data[].first_name").transform(data)

for data in j["data"]: 
    for k, v in data.items():
        if "@reqres.in" in str(v):
            print(v)
