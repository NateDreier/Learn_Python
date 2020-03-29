#!/usr/bin/env python3

bo = ['bo jangles', 20, 60000, 'software']
bob = ['bob saggot', 21, 400000, 'hardware']


print("[+] We have name = ['first last', age, salary, 'type of work'] \n")
people = [bo, bob]

for i in people: print(i)
print("\n")
print("[+] printing bo[0].split()[-1]) \n" + bo[0].split()[-1] + "\n")


print("[+] printing people[1][0] \n" + people[1][0] + "\n")


for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20

for i in people: print(i[2])


#pays = [i[2] for i in people]
#print(pays)

pays = map((lambda i: i[2]), people)
print(list(pays))
print("\n")

print(sum(i[2] for i in people))

people.append(['nate theGreat', 12, 20000, 'wannabedev'])
for i in people: print(i)

NAME, AGE, PAY = range(3)
print(bob[NAME])

bill = [['name', 'bobby smoth'], ['age', 20], ['pay', 10000]]
body = [['name', 'body smuth'], ['age', 30], ['pay', 20000]]

peeps = [bill, body]
#print name and moneys
for i in peeps:
    print(i[0][1], i[2][1])

for i in peeps:
    print(i[0][1].split()[-1])
    i[2][1] *= 1.10
for i in peeps: print(person[2])

