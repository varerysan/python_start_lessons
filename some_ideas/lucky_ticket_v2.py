# author: Valery Mosyagin

# Проверка счастливый билет или нет

def is_lucky(ticket):
    d1 = ticket % 10
    d2 = (ticket // 10) % 10
    d3 = (ticket // 100) % 10
    d4 = (ticket // 1000) % 10
    d5 = (ticket // 10000) % 10
    d6 = (ticket // 100000) % 10
    
    return d1 + d2 + d3 == d4 + d5 + d6        
    
    
ticket = int(input("Введите номер билета:"))

if is_lucky(ticket):
    print("Счастливый билет")
else:
    print("Обычный билет")    


