text = input("Введите текст:")

stat = {}

for sym in text:
    stat[sym] = stat.get(sym,0) + 1

for sym,num in stat.items():
    print(sym, "-", num)


