temp = float(input("Введите температуру:"))

if temp < 0:
    print("Лёд")
elif temp > 100:
    print("Пар")
else:
    print("Вода")
    