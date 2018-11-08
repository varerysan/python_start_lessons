# sleep меньше секунды
import time

num_per_sec  = 100
period = 10 # in seconds
for n in range(num_per_sec * period+1):
    value = n / num_per_sec
    print("\r{:.2f} s     ".format(value), end="")
    time.sleep(1 / num_per_sec)
    
print()
