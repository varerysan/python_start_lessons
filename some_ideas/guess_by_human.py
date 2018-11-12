# author: Valery Mosyagin
# Игра. Компьютер задусывет число, человек угадывает
import random

comp = random.randint(1,100)

print("Попробуйти угадать число от 1 до 100.")

while True:
    human = int(input("Введите число:"))
    if comp > human:
        print("Больше")
    elif comp < human:
        print("Меньше")
    else:
        print("Верно! Вы угадали.")
        break
