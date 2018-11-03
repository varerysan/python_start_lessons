# плгоритм поиска максимального элемента в списке, учитывая,
# что список может быть пуст

print("-------- v1 --------")

data = [10,234,34,567,534,17]
max_value = max(data)
print("v1 Max=",max_value)

print("----------- v2 ------------")
data = []
max_value = max(data, default=None)
print("v2 Max=",max_value)
