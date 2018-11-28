width = int(input("Ширина:"))
height = int(input("Высота:"))

print("*" * width)
for n in range(height-2):
    print("*{}*".format(" " * (width-2)))
print("*" * width)

