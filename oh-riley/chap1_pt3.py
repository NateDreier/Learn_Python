#!/usr/bin/env python3

beevus = {'name': 'beevus head', 'age': 20, 'pay': 50000, 'job': 'dev'}
butt = {'name': 'butt head', 'age': 69, 'pay': 100000, 'job': 'nuthing'}
nate = {'name': 'nate washer', 'age': 12, 'pay': 60000, 'job': 'wannabedev'}

db = {}
db['beevus'] = beevus
db['butt'] = butt
db['nate'] = nate
print(db['butt']['name'])
