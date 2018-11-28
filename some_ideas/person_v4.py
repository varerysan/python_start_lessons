# surname, name, passport, birth
data = [ ["Иванов", "Николай", "123", "19990105"],
         ["Петров", "Иван", "456", "19900604"],
         ["Сидоров", "Петр", "100", "19980723"] ]

print("Все данные:")
for d in data:
    print( d )

print("\n")

print("""По какому полю искать:
1. Фимилия
2. Имя
3. Паспорт
4. День рождения""")

field = int(input("Введите номер:"))

if field < 1 or field > 4:
    print("Надо выбрать 1-4.")
else:
    search = input("Что искать:")
    find = [x for x in data if x[field-1] == search ]
    if find:
        print("Найдено:")
        for person in find:
            print("Фамилия:", person[0])
            print("Имя:", person[1])
            print("Паспорт:", person[2])
            print("Д.р.:", person[3])

#find = [x for x in data if x[2] == passport ]

#print("find=", find)

#for d in data:
#    if d[2] == passport:
#        print("Найдено:")
#        print("Фамилия:", d[0])
#        print("Имя:", d[1])
#        print("Паспорт:", d[2])
#        print("Д.р.:", d[3])

