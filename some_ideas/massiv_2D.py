# example how to create 2D array
# Author: Valery Mosyagin
data = [ [0 for x in range(5) ] for k in range(3)]

print("data=", data)

data[0][0] = 100
data[1][0] = 200

print("data=", data)

print("----------------")
for y in range(3):
    for x in range(5):
        print("{:4}".format(data[y][x]), end="")
    print()

