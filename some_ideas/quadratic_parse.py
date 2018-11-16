# author: Valery Mosyagin
# разбор выражения квадратного уравнения
# 5x^2+7x-25=0
# 5*x*x - 10*x + 5 = 0
# 5*x**2 + 7*x -10 =0
#
#
#

import re


def parse(equation):
    eq = re.sub(" ", "", equation)
    t1, t2  = re.split("=", eq)

    tokens = re.findall("[-\+]?[^\+-]+", t1)

    data = []
    for n in tokens:
        if n:
            if n[0] == "+":
                token = {"sign": "+", "token": n[1:]}
            elif n[0] == "-":
                token = {"sign": "-", "token": n[1:]}
            else:
                token = {"sign": "+", "token": n}
            data.append(token)    
            
    return data

def parse_tokens(tokens):
    data = {'x^2':[], 'x':[], '1':[]}
    for t in tokens:
        t3 = re.split("\*", t['token'])
        print("t3=", t3)
        
        #dat = 
        dat = {}
        for t4 in t3:
            try:
                f = float(t4)
                print("f=", f)
                dat['value'] = f
            except:
                if t4 == 'x':
                    print("t4=x")
                    dat['var'] = 'x'
                elif t4 == 'x^2':
                    print("t4=x^2")
                    dat['var'] = 'x^2'
                else:
                    print("t4=error")  
                    
        
                                

def test(text):
    print("----------------")
    print("eq={}=".format(text))
    tokens = parse(text)
    print("tokens=", tokens)
    parse_tokens(tokens)

    
#-------------------------

#text = " 10*x^2 + 20*x - 7 = 0"
text = "-x^2-25=0"
text = "5*x*x - 10*x + 5 = 0"


test(" 10*x^2 + 20*x - 7 = 0")
test("-x^2-25=0")
test("5*x*x - 10*x + 5 = 0")
test("7.2*x^2 - 10.15*x + 1.5 = 0")


