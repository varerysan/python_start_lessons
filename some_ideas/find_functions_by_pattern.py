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



obj_list = {k:v for k,v in globals().items() if callable(v) and k.endswith("_new")}
for name, obj in obj_list.items():
    print("name=", name, " obj=", obj)


print("-------- call all new functions --------")

for f in obj_list.values(): f()


    
    

