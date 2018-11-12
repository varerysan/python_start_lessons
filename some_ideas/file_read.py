# -*- coding: utf-8 -*-
# author: Valery Mosyagin
# работа с фалами

with open("file_data.txt","r") as file:
    for line in file:
        line2 = line.rstrip("\n")
        print("Line={}=".format(line2))
        
