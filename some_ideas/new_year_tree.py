# Draw New Year Tree in text mode
# Author: Valery Mosyagin

def draw_part(center, begin, end):
    for x in range(begin, end+1):
        print( " " * (center-x), "*" * (x*2+1), sep="") 

def draw_stvol(center, width, height):
    for y in range(height):
        print( " " * (center-width),"*" * (width*2+1), sep="") 

draw_part(30,0,4)
draw_part(30,3,5)
draw_part(30,4,7)
draw_stvol(30,1,4)