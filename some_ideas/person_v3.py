# surname, name, passport, birth
data = [ ["Иванов", "Николай", 123, "19990105"],
         ["Петров", "Иван", 456, "19900604"],
         ["Сидоров", "Петр", 100, "19980723"] ]

print("Все данные:")
for d in data:
    print( d )

print("\n")

print("--- Поиск ---")

passport = int(input("Введите номер паспорта:"))

for d in data:
    if d[2] == passport:
        print("Найдено:")
        print("Фамилия:", d[0])
        print("Имя:", d[1])
        print("Паспорт:", d[2])
        print("Д.р.:", d[3])

