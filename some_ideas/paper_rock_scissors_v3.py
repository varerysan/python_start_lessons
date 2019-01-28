import random

#beat = {'камень':['ножницы','ящерица'], 
#         'ножницы':['бумага','ящерица'],
#         'бумага':['камень','Спок'],
#         'ящерица':['Спок','бумага'],
#         'Спок':['ножницы', 'камень']}


def game_step():
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
        return (0,0)
    elif comp in beat[user]:
        print("Вы победили!")
        return (1,0)
    else:
        print("Вы проиграли.")
        return (0,1)



def game():
    count_user = 0
    count_comp = 0
    while count_user != 3 and count_comp != 3:
        u,c = game_step()
        count_user += u
        count_comp += c
        print("User=",count_user, " Comp=", count_comp)


game()    