# распечатать введеное число по-русски
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
    return  [  [ "тысяч", "ж"],
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
    if pos > 0:
        suffix = ["","а","ов"]
    else:
        suffix = ["а","и",""]
    return base_names[pos][0] + suffix[form]
        
def get_rod(pos):
    names = get_base_names()
    return names[pos][1]
    

nums = [1, 2, 5]

    
#number = int(input("Введите число:"))
#text = say_number(number)
#print("Текст:", text)

for pos in range(5):
    text = ""
    for number in nums:
        word = str(number) + " " + create_word(pos, number)
        text += word + ", "
    print(text)
    
    
for n in range(10):
    number = random.randint(0,999)
    for pos in [0,1,2]:
        rod = get_rod(pos)
        text = say_3(number,rod)
        text += " " + create_word(pos, number)        
        print("{}: {}".format(number,text))



#for n in range(1000):
#    print(n,"==={}===".format(say_3(n,"м")))
