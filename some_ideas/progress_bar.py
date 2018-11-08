# progress bar
# author: Valery Mosyagin
from time import sleep

def draw_progress_bar(width, value):
    
        
    show_value = min(width, int(width * value * 0.01))

    print("[", end="")
    
    symbol = "\u2588" #"\u2592" # 2592, 2593
    symbol_space = "\u2591"

    print( symbol * show_value, end="" )
    print( symbol_space * (width-show_value), end="")
    
    print("]", end="")
    print("  {} %".format(value), end="")
        
    
def draw_progress_bar_v2(width, value):
    
    show_value = min(width*8, int(8*width * value * 0.01))
    
    rest = show_value % 8
    div = show_value // 8
    
    num_spaces = width - div
    
    # https://en.wikipedia.org/wiki/Block_Elements
    symbols = [" ", "\u258F", "\u258E", "\u258D", "\u258C", "\u258B", "\u258A", "\u2589", "\u2588"]

    print("[", end="")


    print(symbols[8] * div, end="")
    
    if rest != 0:
        print(symbols[rest], end="")
        num_spaces -= 1

    print(symbols[0]* num_spaces, end="")      
    
    print("]", end="")
    print("  {} %".format(value), end="")

#draw_progress_bar_v2(10,20)

num = 20
print("Simple progress bar")
for n in range(101):
    print("\r", end="")
    draw_progress_bar(30,n)
    sleep(0.05)
    
print()
    
print("Precise progress bar")
num = 20
for n in range(101*5):
    print("\r", end="")
    draw_progress_bar_v2(30,n/5)
    sleep(0.01)


print()