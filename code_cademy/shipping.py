#!/usr/bin/python3.6

def ground_shipping(w):
    cost = 0
    if w <= 2:
        cost = (1.5 * w) + 20
    elif w > 2 and w <= 6:
        cost = (3 * w) + 20
    elif w > 6 and <= 10:
        cost = 4


# ground
# 1.5
# 3
# 4
# 4.75
#     flat: 20

# drone
# 4.5
# 9
# 12
# 14.25
#     flat: 0

# premium
#     flat: 125