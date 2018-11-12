# author: Valery Mosyagin

temp = float(input("Введите температуру:"))

if temp < 0:
    print("Лёд")
else: 
    if temp > 100:
        print("Пар")
    else:
        print("Вода")
        
