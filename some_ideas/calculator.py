import operator

text = input("Text:")

a,op,b = text.split()

a = float(a)
b = float(b)

res = None

if op == "+":
    res = a + b
elif op == "*":
    res = a * b
else:
    print("Error!")

if res is not None:
    print("res=", res)

