# author: Valery Mosyagin
# разбор выражения квадратного уравнения
# 5x^2+7x-25=0
# 5*x*x - 10*x + 5 = 0
# 5*x**2 + 7*x -10 =0
#
#
#

import re

text = " 10*x^2 + 20*x - 7 = 0"
text = "-x^2-25=0"
#text = "5*x*x - 10*x + 5 = 0"

t2 = re.sub(" ","",text)
print("t2=",t2)

t3,t4 = re.split("=",t2)
print("t3=", t3)
print("t4=", t4)

t5 = re.findall("[-\+]?[^\+-]+",t3)
print("t5=", t5)
print("-"*10)

coefs = {}

for t6 in t5:
    t7 = re.split("\*",t6)
    print("\nfor t6=", t6)
    print("t7=", t7)
    
    
print("---------")
# get sign
data = []
for n in t5:
    if n:
        if n[0] == "+":
            print("n={} sign=[{}]=".format(n,"+"))
            part = n[1:]
            print("part={}=".format(part))
        elif n[0] == "-":
            print("n={} sign=[{}]=".format(n,"-"))
            part = n[1:]
            print("part={}=".format(part))
        else:
            print("n={} sign=[{}]=".format(n,"+"))
            part = n
            print("part={}=".format(part))  
            
    print("---")
    
