# Показ красивой таблицы с ценами


sym_V = "\u2503"
sym_H = "\u2501"
sym_LT = "\u250F"
sym_RT = "\u2513"
sym_LB = "\u2517"
sym_RB = "\u251b"
sym_MT = "\u2533"
sym_MB = "\u253B"


def print_line_top(width1, width2):
    print(sym_LT + 
          sym_H * width1 + 
          sym_MT +
          sym_H * width2 +
          sym_RT)    

def print_line_bottom(width1, width2):
    print(sym_LB + 
          sym_H * width1 + 
          sym_MB +
          sym_H * width2 +
          sym_RB)

def show_table(table):
    
    width1 = max( [len(k) for k in table.keys() ])
    width2 = max( [len(str(k)) for k in table.values() ])
    
    print_line_top(width1, width2)
    for name, price in table.items():
        print("{}{}{}{}{}".format(sym_V, name.ljust(width1), sym_V, str(price).rjust(width2), sym_V ))
    print_line_bottom(width1, width2)


menu = {"Картошка":25, "Суп": 17, "Компот": 12}

show_table(menu)
