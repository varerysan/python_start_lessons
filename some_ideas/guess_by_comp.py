# Человек задумывает число, а компьютер угадывает

min_human = 1
max_human = 100

while True:
    print("min_human=",min_human)
    print("max_human=",max_human)
    mid_human = (min_human + max_human) // 2
    print("Это", mid_human,"?")
    print("1. Вы загадали меньше")
    print("2. Вы загадали больше")
    print("3. Я угадал")
    answer = input("Введите ваш выбор:")
    
    if answer == "1":
        max_human = mid_human - 1
    elif answer == "2":
        min_human = mid_human + 1
    elif answer == "3":
        print("Ура!")
        break
    
print("Игра закончена")

