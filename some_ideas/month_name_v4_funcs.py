# author: Valery Mosyagin

# по названию месяца определяется сезон

def get_season(month_name):
    names = {"январь"  : "Зима",
             "февраль" : "Зима",
             "март"    : "Весна",
             "апрель"  : "Весна",
             "май"     : "Весна",
             "июнь"    : "Лето",
             "июль"    : "Лето",
             "август"  : "Лето",
             "сентябрь": "Осень",
             "октябрь" : "Осень",
             "ноябрь"  : "Осень",
             "декабрь" : "Зима"}
    return names.get(month_name.lower(), None)
        

month_name = input("Введите название месяца:")
season = get_season(month_name)

if season:
    print("Сезон:", season)
else:
    print("Ошибка. Неправильное название месяца")    
