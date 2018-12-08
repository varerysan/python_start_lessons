# example how to create 2D array
import sys
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

d1 = [ x/10.0 for x in range(10000) ]
print("d1 ( 10000 )size=", sys.getsizeof(d1))

d2 = [ x/10.0 for x in range(100000) ]
print("d2 ( 100000 )size=", sys.getsizeof(d2))

d3 = [ x/10.0 for x in range(1000000) ]
print("d3 ( 1000000 )size=", sys.getsizeof(d3))
