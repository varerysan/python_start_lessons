# author: Valery Mosyagin
# Определение подходит ли температура для купания
# Для каждого пользователя свои предпочтительные границы температур

data = {'John':[15,40],
        'Anna':[17,38],
        'Belle':[12,41]}

name = input('Введите своё имя:')
if name not in data:
    print("Информации по такому пользователю нет.")
else:    
    minTemp, maxTemp = data[name]
    temp = int(input("Введите температуру воды:"))
    
    if temp >= minTemp and temp <= maxTemp:
        print("Хорошая температура воды.")
    else:
        print("Температуры воды не очень.")
