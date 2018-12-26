
data = "aaa bbb ccc ddd eee".split()

gen1 = ("g1_"+d for d in data)

data[1] = "new_value"

gen2 = ("g2_"+d for d in data)

print("gen1=", list(gen1))

print("gen2=", list(gen2))
