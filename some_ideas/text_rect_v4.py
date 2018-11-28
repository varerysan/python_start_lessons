width = int(input("Ширина:"))
height = int(input("Высота:"))
num = int(input("Количество:"))

for n in range(num):
    print(  ("*" * width)," " , end=""  )

print()

for n in range(num):
    for y in range(height-2):
        print("*{}*".format(  " " *(width-2)  ), " ", end="")
    print()

for n in range(num):
    print(  ("*" * width)," " , end=""  )

print()
