# author: Valery Mosyagin
# class method override

class A:
    def __init__(self, name):
        self._name = name
        
    def __bool__(self):
        if self._name == "test":
            return True
        else:
            return False
        
    def __call__(self, id):
        print("called by () name={}= id={}=".format(self._name, id))
        

a = A("hello")
b = A("test")

if a:
    print("a is OK")
else:
    print("a is not OK")

if b:
    print("b is OK")
else:
    print("b is not OK")
    
a(100)
b(200)

