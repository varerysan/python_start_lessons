# author: Valery Mosyagin

spisok = [10, 20, 30]
print(spisok)
for value in spisok:
    print("Value={}".format(value))
    
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers2 = []
for n in range(10):
    numbers2.append(n)
    
print("Numbers2=", numbers2)

numbers3 = []
for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    numbers3.append(n)
print("Numbers3=", numbers3)

numbers4 = list(range(10))
print("Numbers4=", numbers4)

two_lists = list(range(100,105)) + list(range(200,205))
print("two_lists=", two_lists)



    
