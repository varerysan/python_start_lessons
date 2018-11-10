import time

def show_field(field,width,height):
    for y in range(height):
        for x in range(width):
            if field[y*width+x]:
                print("O", end="")
            else:
                print(" ", end="")
        print()
        
def move_up(height):
    print("\033[F" * height, end="")
    print("\r", end="")


width = 20
height = 10


pos_x = 5
pos_y = 3
sx = 1
sy = 1

for n in range(100):
    field = []
    for y in range(height):
        for x in range(width):
            if x == pos_x and y == pos_y:
                field.append(1)
            else:
                field.append(0)
    show_field(field, width, height)
    time.sleep(0.03)
    move_up(height)
    pos_x += sx
    pos_y += sy
    if pos_x >= width:
        pos_x = width-1
        sx = -sx

    if pos_x < 0:
        pos_x = 0
        sx = -sx
        
    if pos_y >= height:
        pos_y = height-1
        sy = -sy

    if pos_y < 0:
        pos_y = 0
        sy = -sy
