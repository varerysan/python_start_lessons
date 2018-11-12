# author: Valery Mosyagin

temp = float(input("Введите температуру:"))

if temp < 0:
    print("Лёд")

if temp > 100:
    print("Пар")

if temp >=0 and temp <= 100:
    print("Вода")
    
