# определение по введенному часу времени суток

hour = int(input("Который сейчас час (0-23):"))

if hour < 0 or hour > 23:
    print("Ошибка. Неверное время.")
else:
    if hour < 6 or hour > 22:
        print("Ночь")
    elif hour >= 6 and hour < 12:
        print("Утро")
    elif hour >= 12 and hour < 18:
        print("День")
    else:
        print("Вечер")
