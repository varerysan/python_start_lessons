# распечатать введеное число по-русски

# 0-9
def get_unit(number, rod="м"):
    units = [[""],
             ["один","одна","одно"],
             ["два","две","два"],
             ["три"],
             ["четыре"],
             ["пять"],
             ["шесть"],
             ["семь"],
             ["восемь"],
             ["девять"]]
    
    if len(units[number]) == 1:
        return units[number][0]
    else:
        ids = {"м": 0, "ж": 1, "с": 2}
        return units[number][ids[rod]]
    
# 1-99
def say_number(number, rod="м"):
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
        return get_unit(number, rod)
    
    if number >= 10 and number <=19:
        return ten_units[number-10]
    
    if number >= 20 and number <= 99:
        res = tens[number // 10]
        ed = number % 10
        if ed > 0:
            res += " " + get_unit(number % 10, rod)

        return res
    
def get_name(number, pos):
    text = [ ["тысяча","тысячи","тысяч"],
             ["миллион","миллиона","миллионов"],
             ["миллиард","миллиарда","миллиардов"]             
            ]

    curr_text = text[pos]

    if number == 1:
        return curr_text[0]
    elif number in [2, 3, 4]:
        return curr_text[1]
    elif number in [0, 5, 6, 7, 8, 9]:
        return curr_text[2]
    else:
        return ""        
    
#---------------------------------
#   теория Zero0 - терри Гильям
#=================================
    
def get_hund(number):
    hunds = ["",
             "сто",
             "двести",
             "триста",
             "четыреста",
             "пятьсот",
             "шестьсот",
             "семьсот",
             "восемьсот",
             "девятьсот"]    
    return(hunds[number])
    
    
# 000-999
def say_3(number, rod="м"):
    hund = get_hund(number // 100)
    part2 = say_number(number % 100, rod)
    
    if len(hund) != 0:
        hund += " "
        
    return hund + part2


def get_rod(pos):
    poses = [["тысяча", "ж"]
             ["миллион", "м"]
             ["миллиард", "м"]
              ]

    rods
        
    

    
#number = int(input("Введите число:"))
#text = say_number(number)
#print("Текст:", text)


for n in range(1000):
    print(n,"==={}===".format(say_3(n,"м")))
