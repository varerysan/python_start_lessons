width = int(input("Ширина:"))
height = int(input("Высота:"))
num = int(input("Количество:"))

for n in range(num):
    print("*" * width)
    print(  ("*{}*".format(" " * (width-2))+"\n") * (height-2) , end= ""  )
    print("*" * width)
    print()

