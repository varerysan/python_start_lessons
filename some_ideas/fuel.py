# Определение расхода топлива автомобиля

dist = float(input("Введите расстояние между городами:"))
rash = float(input("Введите расход топлива на 100 км:"))

price = float(input("Введите стоимость литра бензина:"))

parts = dist / 100

fuel = parts * rash
print("Необходимо бензина: {:.2f}".format(fuel))
money = fuel * price
print("Стоимость потраченного бензина: {:.2f}".format(money))
