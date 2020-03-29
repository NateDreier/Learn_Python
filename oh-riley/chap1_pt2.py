#!/usr/bin/env python3

bill = [['name', 'bobby smoth'], ['age', 20], ['pay', 10000]]
body = [['name', 'body smuth'], ['age', 30], ['pay', 20000]]

peeps_list = [bill, body]

#for i in peeps_list:
#    for (name, value) in i:
#        if name == 'name': 
#            print(value)

def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue
#print(field(body, 'pay'))

for i in peeps_list:
    print(field(i, 'age'))

beevus = {'name': 'beevus head', 'age': 20, 'pay': 50000, 'job': 'dev'}
butt = {'name': 'butt head', 'age': 69, 'pay': 100000, 'job': 'nuthing'}
nate = {'name': 'nate washer', 'age': 12, 'pay': 60000, 'job': 'wannabedev'}

peeps_dict = [beevus, butt, nate]

#print(butt['name'], nate['name'])
#print(nate['name'].split()[-1])

for i in peeps_dict:
    print(i['name'], i['pay'], sep=', ')

names = [i['name'] for i in peeps_dict]
#print(names)
#print(sum(i['pay'] for i in peeps_dict))

# Nested dicts

beevus2 = {'name': {'first': 'beevus', 'last': 'head'},
           'age': 32,
           'job': ['wash', 'up'],
           'pat': (30000, 40000)}
butt2 = {'name': {'first': 'butt', 'last': 'head'},
           'age': 69,
           'job': ['wash', 'up'],
           'pat': (60000, 20000)}
peeps_nest = [beevus2, butt2]
#print(beevus2['name'], beevus2['name']['last'])
