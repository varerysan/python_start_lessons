# Sizeof data
# Author: Valery Mosyagin

import sys

d1 = [ x/10.0 for x in range(10000) ]
print("d1 ( 10000 )size=", sys.getsizeof(d1))

d2 = [ x/10.0 for x in range(100000) ]
print("d2 ( 100000 )size=", sys.getsizeof(d2))

d3 = [ x/10.0 for x in range(1000000) ]
print("d3 ( 1000000 )size=", sys.getsizeof(d3))
