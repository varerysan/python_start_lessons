# Test some bit operations
# Author: Valery Mosyagin

def print_bin(value, num_bits=8):
    text = ""
    for _ in range(num_bits):
        text = ("1" if value & 1 == 1 else "0") + text
        value >>= 1
    print(text)



a = 192


for k in range(8):
    b = a & 1
    print("1" if b else "0")
    a = a >> 1

print("------------")

print_bin( 192, 8)

