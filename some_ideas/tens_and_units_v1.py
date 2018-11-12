# Разбиение двузначного числа на десятки и единицв
# author: Valery Mosyagin

number = int(input("Введите двузначное число:"))

ed = number % 10
des = number // 10

print("Десятков:", des)
print("Единиц:", ed)
