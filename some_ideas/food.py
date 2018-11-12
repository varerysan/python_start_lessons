#!/usr/bin/env python3
# author: Valery Mosyagin

def print_menu(m):
    print()
    print("+------ Меню -------+")
    for eda,price in m.items():
        print("|{:<10}: {:>3} руб|".format(eda,price))
    print("+-------------------+")
    
def print_zakaz(z):
    print("+------ Заказ -------+")
    total = 0
    for eda,price in z:
        print("|{:>10}: {:>3} руб|".format(eda,price))
        total += price
    print("+-------------------+") 
    print("|Всего     : {:>3} руб|".format(total))
    print("+-------------------+") 
    
    
menu = {"Суп":10,"Картошка":20,"Компот":15,"Авокадо":37}

zakaz = []

while True:
    print_menu(menu)
    get = input("Что выбираете?")
    
    if not get:
        break
    
    res = menu.get(get,None)
    if res:
        zakaz.append([get,res])
        print_zakaz(zakaz)
    else:
        print("Этого нет в меню")
        
print_zakaz(zakaz)


