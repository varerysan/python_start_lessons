# author: Valery Mosyagin
# разбор выражения квадратного уравнения
# 5x^2+7x-25=0
# 5*x*x - 10*x + 5 = 0
# 5*x**2 + 7*x -10 =0
#
#
#

import re

text = " - 10*x^2 + 20*x - 7 = 0"

t2 = re.sub(" ","",text)
print("t2=",t2)

t3 = re.split("=",t2)
print("t3", t3)
