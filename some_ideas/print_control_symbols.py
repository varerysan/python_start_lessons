import sys
import time
for n in range(10):
    print(n, "kjhskfhwfhwiuefhwief")
    
print("---------------")
print("wait")
time.sleep(1)

for v in range(5):
    sys.stdout.write("\033[F") 

print("================")