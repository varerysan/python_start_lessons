# not finished

import random

digits09 = list(range(10))

#print(digits09)

random.shuffle(digits09)
digits09=["9","3", "0", "5"]

print("digits09=",digits09)

comp = [str(v) for v in digits09[0:4]]

#print("comp=",comp)




while True:

    human = input("Выш выбор=")

    #zz = list(zip(comp, human))

    #print("zz=", zz)

    #for z in zz:
    #    print("z=", z)


    #g1 = [z for z in zz]

    cows_list = [z for z in zip(comp, human) if z[0] != z[1] ]
    bulls_list = [z for z in zip(comp, human) if z[0] == z[1] ]

    bulls = 4 - len(cows_list)

    print("bulls2=", bulls)

    print("cows_list=", cows_list)
    print("bulls_list=", bulls_list)

    #print("g1=", g1)

    break


    bulls = 0

    compCow = []
    humanCow = []

    #  подсчитаем быков
    for n in range(4):
        if comp[n] == human[n]:
            bulls += 1
        else:
            compCow.append(comp[n])
            humanCow.append(human[n])

    print("Быков (полных совпадений):", bulls)
#    print("compCow=", compCow)
#    print("humanCow=", humanCow)

    # Подсчитаеи коров
    cows = 0
    for m in humanCow:
        if m in compCow:
            cows += 1
            compCow.remove(m)
 #           print("new cow=",cows, " compCow=", compCow)


    print("Коров (не на своих местах):", cows)
    if bulls == 4:
        print("Вы победили")
        break


        
