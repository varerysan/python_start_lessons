objects = ['камень','ножницы','бумага']

beat = {0:[1], 
        1:[2],
        2:[0]}



print(beat.keys())

#val1 = 0
#val2 = 1

#name1 = objects[val1]
#name2 = objects[val2]

#print("name1=", name1, " name2=", name2)


#if val2 in beat[val1]:
#    print(name1,"beats",name2)
#else:
#    print(name2,"beats",name1)


for v1 in range(3):
    for v2 in range(v1+1):
        n1 = objects[v1]
        n2 = objects[v2]

        if v1 == v2:
            print(n1,"==",n2)
        else:             
            if v2 in beat[v1]:
                print(n1,"сильнее чем",n2)
            else:
                print(n2,"сильнее чем",n1)

