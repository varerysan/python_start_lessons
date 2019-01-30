n = int(input("Number:"))

divs = {}


for k in range(2,n+1):
    while n % k == 0:
        divs[k] = divs.get(k,0) + 1
        n = n / k

    if n == 1:
        break

full = []
for k,v in divs.items():
    
    kk = [str(k)] * v
    bb = "*".join(kk)
    #print( bb )
    full.append(bb)


print( "*".join(full) )



#print(full)
          
