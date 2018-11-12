# author: Valery Mosyagin

class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def print(self):
        print("Human: {}, {}".format(self._name, self._age))
        
    def __lt__(self, other):
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

print("----- sorted v1 -------")
data1 = sorted(data,  key = lambda v: v.get_age() ) 
    
for d in data1:
    d.print()

print("----- sorted v2 -------")
data2 = sorted(data) 
    
for d in data2:
    d.print()
    
print("----- min v2 -------")
min_value_2 = min(data) 

min_value_2.print()
    
