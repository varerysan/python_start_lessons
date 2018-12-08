import array

ar = array.array('B', [0,10,20,30,255])

tc = ar.typecode

print("tc=", tc)

file = open("data/array_data.dat","wb")

ar.tofile(file)
file.close()

ar.extend([0xA0, 0xB0])

file2 = open("data/array_data2.dat","wb")
ar.tofile(file2)
file2.close()

