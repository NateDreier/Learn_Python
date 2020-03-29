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

print(butt['name'], nate['name'])
print(nate['name'].split()[-1])
