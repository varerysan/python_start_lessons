# Проверка счастливый билет или нет

ticket = int(input("Введите номер билета:"))

print("ticket={}=".format(ticket))

d1 = ticket % 10
d2 = (ticket // 10) % 10
d3 = (ticket // 100) % 10
d4 = (ticket // 1000) % 10
d5 = (ticket // 10000) % 10
d6 = (ticket // 100000) % 10

print("Ticket: {}{}{}{}{}{}".format(d6, d5, d4, d3, d2, d1))

sum1 = d1 + d2 + d3
sum2 = d4 + d5 + d6

if sum1 == sum2:
    print("Счастливый билет")
else:
    print("Обычный билет")
