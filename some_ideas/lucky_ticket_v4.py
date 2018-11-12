# author: Valery Mosyagin

# Проверка счастливый билет или нет

def get_sum(part):
    return sum([int(n) for n in part] )


def is_lucky(ticket):
    numbers = (str(ticket)).zfill(6)
    sum1 = get_sum(numbers[:3])
    sum2 = get_sum(numbers[3:])
    return sum1 == sum2
         

def get_number():
    number = 0
    for ticket in range(1000000):
        if is_lucky(ticket):
            number += 1
    return number
            

number = get_number()
print("Общее число счастливых билетов:", number)
