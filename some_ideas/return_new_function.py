# Проверка возврата новой функуии
# Author: Valery Mosyagin

def base_func():
    print("this is base_func")


def new_func():
    print("Start new_func")
    new_func = base_func
    print("End new_func")


#print("--- main ---")
#print("test run base:")
#base_func()
print("--- test run new ---")
new_func()
print("--- test run new v2 ---")
new_func()

