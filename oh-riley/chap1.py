#!/usr/bin/python3

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
