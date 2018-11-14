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
    
@decor
@decor
def test2():
    print("test2")

print("=" * 30)    
test()

print("=" * 30)    
test2()
print("=" * 30)    
