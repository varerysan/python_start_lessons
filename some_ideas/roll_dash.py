#roll the dash
# author: Valery Mosyagin

from time import sleep
symbols = ["|", "/", "-", "\\" ]

for n in range(10):
    for s in symbols:
        print("\r{}".format(s),end='')
        sleep(0.1)
        
print()
