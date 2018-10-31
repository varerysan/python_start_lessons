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
    
    
number = int(input("Введите число:"))
text = say_number(number)
print("Текст:", text)