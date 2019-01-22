import random

beat1 = {'камень':['ножницы'], 
        'ножницы':['бумага'],
        'бумага':['камень']}


beat = {'камень':['ножницы','ящерица'], 
         'ножницы':['бумага','ящерица'],
         'бумага':['камень','Спок'],
         'ящерица':['Спок','бумага'],
         'Спок':['ножницы', 'камень']}

names = list(beat.keys())
print("Доступные предметы:", names)

user = input("Ваш выбор:")
comp = random.choice(names)
#comp = random.SystemRandom().choice(names)

print("Компьютер выбрал:", comp)

if user == comp:
    print("Ничья.")
elif comp in beat[user]:
    print("Вы победили!")
else:
    print("Вы проиграли.")