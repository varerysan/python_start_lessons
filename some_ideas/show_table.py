# Показ красивой таблицы с ценами
# author: Valery Mosyagin

def print_line(width1, width2):
    print("+" + 
          "-" * width1 + 
          "+" +
          "-" * width2 +
          "+")    

def show_table(table, width1, width2):
    print_line(width1, width2)
    for name, price in table.items():
        print("|{}|{}|".format( name.ljust(width1), str(price).rjust(width2) ))
    print_line(width1, width2)


menu = {"Картошка":25, "Суп": 17}

show_table(menu,10,3)
