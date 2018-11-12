# Разбиение трёхзначного числа на сотни, десятки и единицы
# author: Valery Mosyagin

while True:
    number = int(input("Введите трёхзначное число:"))
        
    if number < 100 or number > 999:
        print("Это не трёхзначное число. Повторите ввод.")
    else:
        break

sot = number // 100
ed = number % 10
des = (number % 100) // 10

print("Сотен:", sot)
print("Десятков:", des)
print("Единиц:", ed)
