import operator

text = input("Text:")

vals = text.split()

if len(vals) != 3:
    print("Error. Need 3 params")
else:

    a = float(vals[0])
    b = float(vals[2])
    op = vals[1]

    res = None

    if op == "+":
        res = a + b
    elif op == "*":
        res = a * b
    else:
        print("Error!")

    if res is not None:
        print("res=", res)

