#

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
        
        
def fill_field(field, width, height):
    for y in range(height):
        field[y*width+0] = 1
    for y in range(height):
        field[y*width+height-1] = 1        
        
def test_field():
    width = 30
    height = 20
    field = []
    for y in range(width):
        for x in range(height):
            field.append(0)
    fill_field(field, width, height)
    show_field(field, width, height)

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


