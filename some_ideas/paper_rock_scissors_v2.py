import random

beat = {'камень':['ножницы'], 
        'ножницы':['бумага'],
        'бумага':['камень']}

names = list(beat.keys())
print("Доступные предметы:", names)

user = input("Ваш выбор:")
comp = random.choice(names)

print("Компьютер выбрал:", comp)

if user == comp:
    print("Ничья.")
elif comp in beat[user]:
    print("Вы победили!")
else:
    print("Вы проиграли.")