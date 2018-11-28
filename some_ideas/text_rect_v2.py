width = int(input("Ширина:"))
height = int(input("Высота:"))

print("*" * width)
print(  ("*{}*".format(" " * (width-2))+"\n") * (height-2) , end= ""  )
print("*" * width)

