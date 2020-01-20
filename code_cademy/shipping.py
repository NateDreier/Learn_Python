#!/usr/bin/python3.6
#Death by ifs
import random

def ground_shipping(w):
    cost = 0
    if w >= 0:
        if w <= 2:
            cost = (1.5 * w) + 20
        elif w > 2 and w <= 6:
            cost = (3 * w) + 20
        elif w > 6 and w <= 10:
            cost = (4 * w) + 20
        else:
            cost = (4.75 * w) + 20
        return cost
    else:
        return("weight needs to be 0 or greater")
    

def drone_shipping(w):
    cost = 0
    if w >= 0:
        if w <= 2:
            cost = (4.5 * w)
        elif w > 2 and w <= 6:
            cost = (9 *w)
        elif w > 6 and w <= 10:
            cost = (12 * w)
        else:
            cost = (14.25 * w)
        return cost
    else:
        return("weight needs to be 0 or greater")

def premium_shipping():
    cost = 125
    return(cost)

#packageWeight = int(input('Enter the packages weight'))
packageWeight = random.randint(1, 25)
#print(str(packageWeight) + "\n")


ground = ground_shipping(packageWeight)
drone = drone_shipping(packageWeight)
premium = premium_shipping()

if (ground < drone and ground < premium):
    print("Groung shipping is your cheapest option.")
elif (drone < ground and drone < premium):
    print("The new Drone shipping is your cheapest option")
else:
    print("Premium shipping is your cheapest option")


# premium
#     flat: 125