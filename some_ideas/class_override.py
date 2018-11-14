# author: Valery Mosyagin
# class method override

# https://pythonworld.ru/osnovy/peregruzka-operatorov.html

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
        
    def __getitem__(self, key):
        print("called by [] ={}=".format(key))
        
    def __str__(self):
        return "convert to string name={}=".format(self._name)
        

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

a[123]

#convert to string
string = str(a)
print("string:", string)

