#
import math


symbols = [" ","\u2581","\u2582","\u2583","\u2584","\u2585","\u2586","\u2587","\u2588"]


def show_vals(data):
    for val in data:
        print(symbols[val],end="")
        
        

def create_sin():
    data = []
    for x in range(30):
        y = int((math.sin(x / 3) + 1)* 7 / 2)
        if y < 0:
            y = 0
        elif y > 7:
            y = 7
        data.append(y)
    return data

data = create_sin()            
print("data=", data)
            
    
    

