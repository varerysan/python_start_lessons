import random

digits09 = list(range(10))

#print(digits09)

random.shuffle(digits09)
digits09=["9","3", "0", "5"]

#print("digits09=",digits09)

comp = [str(v) for v in digits09[0:4]]

#print("comp=",comp)

while True:

    human = input("Выш выбор=")

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


        
