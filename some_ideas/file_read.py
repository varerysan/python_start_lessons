# -*- coding: utf-8 -*-
# работа с фалами

with open("file_data.txt","r") as file:
    for line in file:
        print("Line={}=".format(line))
        
