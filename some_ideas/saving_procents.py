base = float(input("Amount:"))
proc = float(input("Procents:"))
num = int(input("Number of years:"))

amount = base

for n in range(num):
    print("Year",n)
    print("  Begin amount=", amount)
    amount += amount * (proc / 100)
    print("  End amount=", amount)


print("result=", amount)

extra = amount - base
print("Extatra=", extra)
rate = amount / base

print("Rate=", rate)