# простой пример небольшой базы даннх людей

class Person:
    def __init__(self):
        self._name = ""
        self._second_name = ""
        self._birth_year = None
        
    def print(self):
        print("Name:", self._name)
        print("Second name:", self._second_name)
        print("Birth year:", self._birth_year)
        
    