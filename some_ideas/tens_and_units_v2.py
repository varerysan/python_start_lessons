# Разбиение двузначного числа на десятки и единицв
# author: Valery Mosyagin

while True:
    number = int(input("Введите двузначное число:"))
        
    if number < 10 or number > 99:
        print("Это не двузначное число. Повторите ввод.")
    else:
        break

ed = number % 10
des = number // 10

print("Десятков:", des)
print("Единиц:", ed)
