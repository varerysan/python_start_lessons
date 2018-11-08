# progress bar
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
    div = show_value / 8
    
    

    #print("[", end="")
    
    
    symbols = [" ", "\u258F", "\u258E", "\u258D", "\u258C", "\u258B", "\u258A", "\u2589", "\u2588"]
    
    print(symbols)
    
    return
    
    symbol = "\u2588" #"\u2592" # 2592, 2593
    symbol_space = " "

    print( symbol * show_value, end="" )
    print( symbol_space * (width-show_value), end="")
    
    print("]", end="")
    print("  {} %".format(value), end="")
        

draw_progress_bar_v2(10,20)
    
num = 20
for n in range(101*0):
    print("\r", end="")
    draw_progress_bar(30,n)
    sleep(0.1)


print()