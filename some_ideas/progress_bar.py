# progress bar
from time import sleep

def draw_progress_bar(width, value):
    
        
    show_value = min(width, int(width * value * 0.01))

    print("[", end="")
    
    symbol = "\u2592" # 2592, 2593
    symbol_space = "\u2591"

    print( symbol * show_value, end="" )
    print( symbol_space * (width-show_value), end="")
    
    print("]", end="")
    print("  {} %".format(value), end="")
        
num = 20
for n in range(101):
    print("\r", end="")
    draw_progress_bar(30,n)
    sleep(0.1)


print()