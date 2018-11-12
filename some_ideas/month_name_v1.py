# author: Valery Mosyagin

# по номеру месяца выводим его название

month = int(input("Ввелите номер месяца (1-12):"))

if month < 1 or month > 12:
    print("Неверный номер")
else:
    if month == 1:
        print("Январь")
    elif month == 2:
        print("Февраль")
    elif month == 3:
        print("Март")
    elif month == 4:
        print("Апрель")
    elif month == 5:
        print("Май")
    elif month == 6:
        print("Июнь")
    elif month == 7:
        print("Июль")
    elif month == 8:
        print("Август")
    elif month == 9:
        print("Сентябрь")
    elif month == 10:
        print("Октябрь")
    elif month == 11:
        print("Ноябрь")
    elif month == 12:
        print("Декабрь")
    
    
