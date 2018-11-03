
class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def print(self):
        print("Human: {}, {}".format(self._name, self._age))
        
        

h = Human("John", 23)
h.print()
        