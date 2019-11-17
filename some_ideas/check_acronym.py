#!/usr/bin/env python3

print("Test for acronym:")
line1 = input("Input line1:")
line2 = input("Input line2:")

counter1 = {}
counter2 = {}

for sym in line1:
    counter1[sym] = counter1.get(sym, 0) + 1

for sym in line2:
    counter2[sym] = counter2.get(sym, 0) + 1


print("Counter={}".format(counter1))
print("Counter={}".format(counter2))

if counter1 == counter2:
    print("Equals")
else:
    print("Not equals")
