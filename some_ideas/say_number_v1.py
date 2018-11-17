# распечатать введеное число по-русски
# author: Valery Mosyagin

import random
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


def get_base_names():
    return  [  [ "", "м" ],
               [ "тысяч", "ж"],
               [ "миллион", "м"],
               [ "миллиард", "м"],
               [ "триллион", "м"],
               [ "квадриллион", "м"],
               [ "квинтиллион", "м"],
               [ "секстиллион", "м"],
               [ "септиллион", "м"],
               [ "октиллион", "м"],
               [ "нониллион", "м"],
               [ "дециллион", "м"],
               [ "ундециллион", "м"],
               [ "додециллион", "м"],
               [ "тредециллион", "м"],
               [ "кваттуордециллион", "м"],
               [ "квиндециллион", "м"],
               [ "сексдециллион", "м"],
               [ "септемдециллион", "м"],
               [ "октодециллион", "м"],
               [ "новемдециллион", "м"],
               [ "вигинтиллион", "м"]	]

def get_form(full_number): 
    number = full_number % 100   
    if number >= 10 and number <= 20:
        return 2   
    ed = number % 10    
    if ed == 1:
        return 0
    elif ed in [2, 3, 4]:
        return 1
    elif ed in [0, 5, 6, 7, 8, 9]:
        return 2


def create_word(pos, number):
    form = get_form(number)
    base_names = get_base_names()
    if pos == 0:
        suffix = ["","",""]
    elif pos > 1:
        suffix = ["","а","ов"]
    else:
        suffix = ["а","и",""]
    return base_names[pos][0] + suffix[form]
        
def get_rod(pos):
    names = get_base_names()
    return names[pos][1]
    

def create_number_and_name(number, pos):
    rod = get_rod(pos)
    text = say_3(number,rod)
    name = create_word(pos, number) if number != 0 else ""
    text += " " + name
    return text        


def split_numer(text_number):
    parts = []
    
    while len(text_number) > 0:
        parts.append(text_number[-3:])
        text_number = text_number[:-3]
        
    parts.reverse()
    return parts
    
def say_parts(parts):
    curr_pos = len(parts) - 1
    full_text = ""
    for part in parts:
        full_text += create_number_and_name(int(part), curr_pos) + " "  
        curr_pos -= 1
    return full_text

def say_full_number(number):
    if number == "0":
        return "ноль"
    return say_parts(split_numer(number))
    

def get_comma_number(number):
    return ",".join(split_numer(number))    

def test_1():
    for pos in range(5):
        text = ""
        for number in [1, 2, 5]:
            word = str(number) + " " + create_word(pos, number)
            text += word + ", "
        print(text)
    

def test_2():
    for n in range(10):
        number = random.randint(0,999)
        for pos in [0,1,2]:
            text = create_number_and_name(number, pos)     
            print("{}: ={}=".format(number,text))
     
def test_3():
    parts = split_numer("36452698492834")
    for p in parts:
        print(p)

def test_4():
    number = "36458979972698492834"
    parts = split_numer(number)
    text_parts = ",".join(parts)
    text = say_parts(parts)
    print(text_parts, ":", text)
    


#test_1()
#test_2()
#test_3()
#test_4()
    
number = input("Введите число:")
#number = "1000101000"
#number = "98034597623497623498740893456982347861348734"
if not number.isdigit():
    print("Это не число")
else:
    text = say_full_number(number)
    comma = get_comma_number(number)
    print(comma, "Текст:", text)
