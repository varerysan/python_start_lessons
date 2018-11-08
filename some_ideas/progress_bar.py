# progress bar

def draw_progress_bar(width, value):
    print("[", end="")
    symbol = "\u2591" # 2592, 2593
    for n in range(width):
        print(symbol, end="")
        
    print("]", end="")
        

draw_progress_bar(30,30)

print()