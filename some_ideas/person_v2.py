#
data = {'Иванов': ['Николай', 11152344, '20010202'],
        'Сидоров': ['Иван', 52352354, '20001205'],
        'Петров': ['Игорь', 324234, '19950107']}

surname = input('Введите фамилию:')

if surname not in data:
    print("Нет такой фамилии")
else:
    print("Фамилия:", surname)
    print("Имя:", data[surname][0])
    print("Паспорт:", data[surname][1])
    print("Д.р.:", data[surname][2])
