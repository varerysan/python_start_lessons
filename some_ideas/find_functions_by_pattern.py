# Ищем все функции в модуле, которые удовлетворяют имени "*_new"
# Author: Valery Mosyagin

def func1():
    print("called func1");

def func2_new():
    print("called func2_new");

def func3_new2():
    print("called func3_new2");

def func4_new():
    print("called func4_new");

def func5_New():
    print("called func5_New");


def find_funcs():
    return  {k:v for k,v in globals().items() if callable(v) and k.endswith("_new")}

def print_funcs(funcs):
    print("Found functions:")
    for name, obj in funcs.items():
        print("Function name=", name, " obj=", obj)
    print()

def call_funcs(funcs):
    for name,f in funcs.items(): 
        print("Call function '{}':".format(name))
        f()
        print()


funcs = find_funcs()
print_funcs(funcs)
call_funcs(funcs)

    
    

