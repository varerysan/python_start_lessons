def fibonacci(num):
    f0 = 0
    f1 = 1
    for k in range(num):
        f2 = f0 + f1
        yield f1
        f0, f1 = f1, f2

for f in fibonacci(5):
    print("fib=", f)
