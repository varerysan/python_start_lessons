# -*- coding: utf-8 -*-
# author: Valery Mosyagin
# работа с фалами. Сортировка чисел из файла
# числа хранятся в файле, в одной стрке может быть несколько чисел
# в строке погут быть пробелы

data = []
with open("file_sort_data.txt","r") as file:
    for line in file.read().split():
        value = int(line)
        print("Value={}=".format(value))
        data.append(value)
        

data_sort = sorted(data)

print("Will write to file:")
print(data_sort)

with open("file_sort_res.txt","w") as res_file:
    for val in data_sort:
        res_file.write(str(val) + "\n")
        



        
