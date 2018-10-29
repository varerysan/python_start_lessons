# Проверка счастливый билет или нет

ticket = int(input("Введите номер билета:"))

print("ticket={}=".format(ticket))

d1 = ticket % 10
d2 = (ticket // 10) % 10
d3 = (ticket // 100) % 10
d4 = (ticket // 1000) % 10
d5 = (ticket // 10000) % 10
d6 = (ticket // 100000) % 10

print()
