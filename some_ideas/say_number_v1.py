# распечатать введеное число по-русски

def say_number(number):
    units = ["ноль",
             "один",
             "два",
             "три",
             "четыре",
             "пять",
             "шесть",
             "семь",
             "восемь",
             "девять"]
    
    tens = ["",
            "десять",
            "двадцать",
            "тридцать",
            "сорок",
            "пятьдесят",
            "шестьдесят",
            "семьдесят",
            "восемьдесят",
            "девяносто"]
    
    ten_units = ["десять",
                 "одиннадцать",
                 "двенадцать",
                 "тринадцать",
                 "четырнадцать",
                 "пятнадцать",
                 "шестнадцать",
                 "семнадцать",
                 "восемнадцать",
                 "девятнадцать"]
    
    if number >=0 and number <= 9:
        return units[number]
    
    if number >= 10 and number <=19:
        return ten_units[number-10]
    
    if number >= 20 and number <= 99:
        ed = number % 10
        res = tens[number // 10]
        if ed > 0:
            res += " " + units[number % 10]

        return res
    
    
number = int(input("Введите число:"))
text = say_number(number)
print("Текст:", text)


for n in range(100):
    print(n,"-", say_number(n))