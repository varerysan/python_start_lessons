# Merge to files with numbers

with open("data1.txt","r") as file1:
    while True:
        line = file1.readline()
   
        if not line:
            break

        print("Line=", line)