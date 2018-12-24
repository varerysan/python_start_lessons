# Data file with numbers given
# Find min, max.
# Add min to begin in file.
# Add max to end of file

file_name = "data/data_min_max_change.txt"

pos = 0

min_val = 0
min_pos = 0

max_val = 0
max_pos = 0

with open(file_name, "r") as file:
    val = int(file.readline())
    min_val = val
    max_val = val

    print("Min=", min_val)
    print("Max=", max_val)
       

    for line in file:
        pos += 1
        n = int(line)
        if n < min_val:
            min_val = n
            min_pos = pos

        if n > max_val:
            max_val = n
            max_pos = pos

        print("n=", n)

    
print("-----------------")
print("Min_val=", min_val, "pos=", min_pos)
print("Max_val=", max_val, "pos=", max_pos)

res_file_name = "data/data_change_res.txt"

with open(res_file_name, "w") as res_file:
    with open(file_name, "r") as file:
        res_file.write(str(min_val) + "\n")
        pos = 0
        for line in file:
            n = int(line)
            if pos not in [min_val, max_val]:
                res_file.write(str(n) + "\n")
        res_file.write(str(max_val) + "\n")
        pos += 1
 


res_file_name2 = "data/data_change_res2.txt"

with open(res_file_name2, "w") as res_file:
    with open(file_name, "r") as file:
        pos = 0
        for line in file:
            n = int(line)
            if pos == min_pos:
                res_file.write(str(max_val) + "\n")
            elif pos == max_pos:
                res_file.write(str(min_val) + "\n")
            else:
                res_file.write(str(n) + "\n")

            pos += 1
 






