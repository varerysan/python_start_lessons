# Проверка можно ли купатьс в воде.
# author: Valery Mosyagin


temp = int(input("Введите температуру воды для купания:"))
if temp > 16 and temp < 40:
    print("Купаться можно.")
else:
    print("Вода не очень.")