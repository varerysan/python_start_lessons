def gen1():
    begin = 10
    while begin <= 20:
        if begin < 20:
            yield begin
        begin += 1

for k in gen1():
    print("k=", k)

