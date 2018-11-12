# author: Valery Mosyagin

#
import math
import time
import random

pixels = [" ", "\u2596", "\u2597", "\u2598", "\u2599", 
          "\u259A", "\u259B", "\u259C", "\u259D", "\u259E", "\u259F",
          "\u258C", "\u2590", "\u2584", 
          "\u2580", 
          ]


blocks = ["\u2580",
          "\u2581",
          "\u2582",
          "\u2583",
          "\u2584",
          "\u2585",
          "\u2586",
          "\u2587",
          "\u2588",
          "\u2589",
          "\u258A",
          "\u258B",
          "\u258C",
          "\u258D",
          "\u258E",
          "\u258F",
          "\u2590",
          "\u2591",
          "\u2592",
          "\u2593",
          "\u2594",
          "\u2595",
          "\u2596",
          "\u2597",
          "\u2598",
          "\u2599",
          "\u259A",
          "\u259B",
          "\u259C",
          "\u259D",
          "\u259E",
          "\u259F"]


sym_blocks = [
              " ",  # 0000
              "\u2597",  # 0001
              "\u2596",  # 0010
              "\u2584",  # 0011
              "\u259D",  # 0100
              "\u2590",  # 0101
              "\u259E",  # 0110
              "\u259F",  # 0111
              "\u2598",  # 1000
              "\u259A",  # 1001
              "\u258C",  # 1010
              "\u2599",  # 1011
              "\u2580",  # 1100
              "\u259C",  # 1101
              "\u259B",  # 1110
              "\u2588"  # 1111
        ]


def show_pixels():
    for s in sym_blocks:
        print("{}=".format(s), end="")
    print("=" * 30)
    

def show_field(field, width, height):
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            d3 = field[y * width + x]
            d2 = field[y * width + x + 1]
            d1 = field[(y+1) * width + x ]
            d0 = field[(y+1) * width + x + 1]
            
            v = d3 * 8 + d2 * 4 + d1 * 2 + d0
        
            s = sym_blocks[v]

            print(s, end="")

        print()
        
def up_field(height):
    print("\033[F" * (height//2), end="")

def put_pixel(field, width, height, x, y):
    if x >=0 and x < width and y >= 0 and y < height:
        field[y*width+x] = 1
        
def fill_field(field, width, height):
    for y in range(height):
        field[y*width+0] = 1
    for y in range(height):
        field[y*width+width-1] = 1 
    for x in range(width):
        field[0*width+x] = 1
    for x in range(width):
        field[(height-1)*width+x] = 1

        

def draw_line(field, width, height, x1, y1, x2, y2):
    delta_x = abs(x1-x2)
    delta_y = abs(y1-y2)
    num = int(max(delta_x, delta_y))
    for n in range(num):
        x = int(x1 + (x2 - x1) * n / num)
        y = int(y1 + (y2 - y1) * n / num)
        put_pixel(field, width, height, x, y)
            

def draw_circle(field, width, height, xc, yc, r):
    num = r * 7
    for n in range(num):
        angle = (math.pi * 2 / num ) * n
        x = int(xc + r * math.cos(angle))
        y = int(yc + r * math.sin(angle))
        put_pixel(field, width, height, x, y)
        
        
def draw_ellipse(field, width, height, xc, yc, rx, ry):
    num = max(rx, ry) * 7
    for n in range(num):
        angle = (math.pi * 2 / num ) * n
        x = int(xc + rx * math.cos(angle))
        y = int(yc + ry * math.sin(angle))
        put_pixel(field, width, height, x, y)
        
        
def clear_field(field):
    for n in range(len(field)):
        field[n] = 0


def update_field(field, width, height):
    show_field(field, width, height)
    up_field(height)      
    

def draw_line_3D(field, width, height, line):
    p0 = line[0]
    p1 = line[1]
    
    x1 = p0[0]
    y1 = p0[1]
    z1 = p0[2]
    
    x2 = p1[0]
    y2 = p1[1]
    z2 = p1[2]
    
    draw_line(field, width, height, x1, y1, x2, y2)
    
    
def draw_object(field, width, height, obj):
    for line in obj:
        draw_line_3D(field, width, height, line)
    
    
def create_object():
    lines = [ [ [ 10, 10,-10],[ 10,-10,-10] ],
              [ [ 10,-10,-10],[-10,-10,-10] ],
              [ [-10,-10,-10],[-10, 10,-10] ],
              [ [-10, 10,-10],[ 10, 10,-10] ],
              
              [ [ 10, 10,-10],[ 10, 10, 10] ], 
              [ [ 10,-10,-10],[ 10,-10, 10] ],
              [ [-10,-10,-10],[-10,-10, 10] ],
              [ [-10, 10,-10],[-10, 10, 10] ],
              
              [ [ 10, 10, 10],[ 10,-10, 10] ],
              [ [ 10,-10, 10],[-10,-10, 10] ],
              [ [-10,-10, 10],[-10, 10, 10] ],
              [ [-10, 10, 10],[ 10, 10, 10] ] ]
        
    return lines 


def rotate_point(pnt, ax, ay, az):
    x = pnt[0]
    y = pnt[1]
    z = pnt[2]
    
    # x - z
    # y - x 
    # z - y 
    
    # rotate by Z
    x1 = x * math.cos(ax) - y * math.sin(ax)
    y1 = x * math.sin(ax) + y * math.cos(ax)
    z1 = z
    
    # rotate by Y
    z2 = z1 * math.cos(ax) - x1 * math.sin(ax)
    x2 = z1 * math.sin(ax) + x1 * math.cos(ax)
    y2 = y1

    # rotate by X
    y3 = y2 * math.cos(ax) - z2 * math.sin(ax)
    z3 = y2 * math.sin(ax) + z2 * math.cos(ax)
    x3 = x2
    
    return [x3,y3,z3]
    

def rotate_object(obj, ax, ay, az, dx, dy ):
    obj2 = []
    for line in obj:
        p1 = rotate_point(line[0], ax, ay, az)
        p2 = rotate_point(line[1], ax, ay, az)
        
        p1[0] *= 2
        p2[0] *= 2
        
        p1[0] += dx
        p1[1] += dy
        
        p2[0] += dx
        p2[1] += dy
        
        
        line2 = [p1, p2]
        obj2.append(line2)
        
    return obj2
        
    
def test_field():
    width = 50*2
    height = 20*2
    field = []
    for y in range(height):
        for x in range(width):
            field.append(0)
    fill_field(field, width, height)
    
    draw_line(field, width, height, 0, 0, width-1, height-1 )
    
    update_field(field, width, height)
    
    time.sleep(1)
       
    clear_field(field)
    for n in range(5):
        x = random.randint(0, width - 1)    
        y = random.randint(0, height - 1)
        draw_circle(field, width, height, x, y, 5)
    update_field(field, width, height)
                
    time.sleep(1)

    clear_field(field)
    for n in range(5):
        x = random.randint(0, width - 1)    
        y = random.randint(0, height - 1)
        draw_ellipse(field, width, height, x, y, 10, 5)
    update_field(field, width, height)
          
    time.sleep(1)
    
    clear_field(field)
    cube = create_object()
    ax = 1.2
    ay = 0.7
    az = 2.1
    
    dax =  0.2 / 2
    day =  0.1 / 2
    daz = -0.1 / 2
        
    dx = width / 2
    dy  = height / 2 
    for n in range(300):
        cube2 = rotate_object(cube, ax, ay, az, dx, dy)
        clear_field(field)
        draw_object(field, width, height, cube2)
        update_field(field, width, height)
        time.sleep(0.03)
        ax +=  dax
        ay +=  day
        az +=  daz
        
        if ax > math.pi * 2:
            ax -= math.pi * 2
        if ax < 0:
            ax += math.pi * 2
            
        if ay > math.pi * 2:
            ay -= math.pi * 2
        if ay < 0:
            ay += math.pi * 2
            
        if az > math.pi * 2:
            az -= math.pi * 2
        if az < 0:
            az += math.pi * 2

    clear_field(field)
    xc = int(width/2)
    yc = int(height/2)
    for r in range(2, 20):
        draw_circle(field, width, height, xc, yc, r)
        time.sleep(0.03)
        update_field(field, width, height)

    time.sleep(1)
    
    clear_field(field)
    xc = int(width/2)
    yc = int(height/2)
    for r in range(2, 20):
        draw_ellipse(field, width, height, xc, yc, r*2, r)
        time.sleep(0.03)
        update_field(field, width, height)

    time.sleep(1)    
    
    clear_field(field)
    x = 5
    y = 3
    sx = 1
    sy = 1
    for n in range(500):
        put_pixel(field, width, height, x, y)
        show_field(field, width, height )
        up_field(height)
        x += sx
        y += sy
        if x < 1 or x > width - 2:
            sx = -sx
        if y < 1 or y > height - 2:
            sy = -sy   
        time.sleep(0.01)
    update_field(field, width, height)
    
    

def show_line():
    for b in blocks:
        print("\u2591{}".format(b), end="")   
        #print("\u2588{}".format(b), end="")   
    print() 
    
    





#for b in blocks:
#    print("\u2591{}|\u2503\u256D\u256E".format(b), end="")   
#print()
#
#for b in blocks:
#    print("\u2591{}".format(b), end="")   
#print()
    
for n in range(32):
    show_line()
    
print("-" * 30)

show_pixels()
    
print()

test_field()


