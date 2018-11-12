# author: Valery Mosyagin
# плгоритм поиска максимального элемента в списке, учитывая,
# что список может быть пуст

data = [10,234,34,567,534,17]


max_val = None
if len(data) > 0:
    max_val = data[0]
    for val in data[1:]:
        if val > max_val:
            max_val = val

print("Max=",max_val)
