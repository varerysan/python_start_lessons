
class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def print(self):
        print("Human: {}, {}".format(self._name, self._age))
        
    def less(self, other):
        return self._age < other._age
    
    def get_age(self):
        return self._age
        
        

h = Human("John", 23)
h.print()
        
data = []
data.append( Human("aaa-123", 123 ))
data.append( Human("aaa-10", 10 ))
data.append( Human("aaa-350", 350 ))
data.append( Human("aaa-27", 27 ))
data.append( Human("aaa-300", 300 ))

value = max(data, key = lambda v: v.get_age() )
value.print()

print("----- sorted -------")
data2 = sorted(data,  key = lambda v: v.get_age() ) 
    
for d in data2:
    d.print()
