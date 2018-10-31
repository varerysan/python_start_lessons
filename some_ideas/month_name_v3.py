# по названию месяца выводим его номер и определяется сезон

month_name = input("Введите название месяца:")

names = ["январь",
         "февраль",
         "март",
         "апрель",
         "май",
         "июнь",
         "июль",
         "август",
         "сентябрь",
         "октябрь",
         "ноябрь",
         "декабрь"]

num = None

try:
    pos = names.index(month_name.lower())
    num = pos + 1  
except ValueError:
    print("Неверное название месяца")

if num:
    if num >= 3 and num <= 5:
        print("Весна")
    elif num >= 6 and num <= 8:
        print("Лето")
    elif num >= 9 and num <= 11:
        print("Осень")
    else:
        print("Зима")
