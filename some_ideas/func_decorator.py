# author: Valery Mosyagin
# Декорирование функций

def decor(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
    
    
@decor
def test():
    print("test function")
    
    
test()