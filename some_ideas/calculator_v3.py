import operator
import re


funcs = {"+": operator.add,
         "-": operator.sub,
         "*": operator.mul,
         "/": operator.truediv}

ops = "".join(funcs.keys())
re_ops = re.escape(ops)
re_exp = re.compile("(.*)([{}])(.*)".format(re_ops))
                           

text = input("Equation (use {}):".format(ops))

m = re.match(re_exp, text)

if not m:
    print("No such operaion")
else:
    vals = m.groups()
    
    try:
        a = float(vals[0])
        b = float(vals[2])
        op = vals[1]

        res = funcs[op](a,b)
        print("res=", res)


    except ValueError:
        print("Error. No correct numbers.")
        
    except ZeroDivisionError:
        print("No div by 0") 



    

#vals = text.split()

#if len(vals) != 3:
#    print("Error. Need 3 params")
#else:

#    a = float(vals[0])
#    b = float(vals[2])
#    op = vals[1]

#    res = None

#    if op == "+":
#        res = a + b
#    elif op == "*":
#        res = a * b
#    else:
#        print("Error!")
#
#    if res is not None:
#        print("res=", res)

