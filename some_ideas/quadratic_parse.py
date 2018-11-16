# author: Valery Mosyagin
# разбор выражения квадратного уравнения
# 5x^2+7x-25=0
# 5*x*x - 10*x + 5 = 0
# 5*x**2 + 7*x -10 =0
#
import re


def parse(equation):
    eq = re.sub(" ", "", equation)
    t1, t2  = re.split("=", eq)

    if t2 != '0':
        raise Exception("BadZeroEnd")
        
    tokens = re.findall("[-\+]?[^\+-]*", t1)

    #print("tokens ===", tokens)

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
    data = []
    for t in tokens:
        dat = {'sign': t['sign']}
        for mul in re.split("\*", t['token']):
            try:
                f = float(mul)
                dat['value'] = f
            except:
                if mul == 'x':
                    dat['var'] = 'x'
                elif mul == 'x^2':
                    dat['var'] = 'x^2'
                else:
                    dat['error'] = True
                    raise Exception("BadToken")
        if 'value' not in dat:
            dat['value'] = 1
            
        if 'var' not in dat:
            dat['var'] = '1'
            
        if dat['sign'] == '-':
            dat['value'] *= -1
        
        del dat['sign']
            
        data.append(dat)        
    return data


def sum_tokens(tokens):
    data = { 'x^2': 0, 'x': 0, '1': 0}
    for t in tokens:  
        data[t['var']] += t['value']     
    return data
                    

def solve(summa):
    a = summa["x^2"]
    b = summa["x"]
    c = summa["1"]
    
    print("a={}, b={}, c={}".format(a,b,c))
    
    

def test(text):
    
    try:
        print("\n\n------ Example -------")
        #print("eq[{}]\n".format(text))
        print(text)
        tokens = parse(text)
        #print("tokens=", tokens)
        data = parse_tokens(tokens)
        
        #print("------ parsed tokens -------")
        #for d in data:
        #    print("d=", d)
            
        summa = sum_tokens(data)
        
        #print("summa=", summa)
        
        solve(summa)
    except:
        print("Error bad token")


test(" 10*x^2 + 20*x - 7 = 5") # error
test("-x^2-25=0")
#test("5*x*x - 10*x + 5 = 0")
test("7.2*x^2 - 10.15*x + 1.5 = 0")
test("x+x-x+x^2-10*x^2=0")
#test("x=0")
#test("5=7")
test("A*x=0")  # error
#test("10.5*x^3-12=0")

test("x+-+x=10") # error
test("x==0")


