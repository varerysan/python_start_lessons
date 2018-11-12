# Проверка существования треугольника по длинам сторон
# author: Valery Mosyagin

len1 = float(input("Введите длину первой рейки:"))
len2 = float(input("Введите длину второй рейки:"))
len3 = float(input("Введите длину третьей рейки:"))


if (len1 < len2 + len3 and
    len2 < len1 + len3 and
    len3 < len1 + len2):
    print("Треугольник можно построить")
else:
    print("Треугольник нельзя построить")
