# author: Valery Mosyagin
# определение по введенному часу времени суток
# с функцией

def get_day_part(hour):       
    if hour < 0 or hour > 23:
        return None

    if hour < 6 or hour > 22:
        part = "Ночь"
    elif hour >= 6 and hour < 12:
        part = "Утро"
    elif hour >= 12 and hour < 18:
        part = "День"
    else:
        part = "Вечер"
            
    return part


hour = int(input("Который сейчас час (0-23):"))
part = get_day_part(hour)

if part:
    print("Сейчас:", part)
else:
    print("Ошибка. Неверное время")
