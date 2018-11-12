# author: Valery Mosyagin

dist = float(input("Введите расстояние между городами:"))
speed = float(input("Введите скорость автомобиля:"))
time = dist/speed
print("Автомобиль доедет за", time, "ч")
print("Автомобиль доедет за {:.2f} ч.".format(time))
