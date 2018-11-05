# простой пример небольшой базы даннх людей

class Person:
    def __init__(self, name, surname, birth):
        self._name = name
        self._surname = surname
        self._birth_year = birth
        
    def print(self):
        print("Name:", self._name)
        print("Surname:", self._surname)
        print("Birth year:", self._birth_year)
        
    def write(self, file):
        file.write(self._name + "\n")
        file.write(self._surname + "\n")
        file.write(str(self._birth_year) + "\n")
        
        


# Cosmos 3M
# лапота. Энергия

class Base:
    def __init__(self):
        self._persons = []
        self._file_name = "db_persons.dat"
    
    def print(self):
        for p in self._persons:
            p.print()
            
    def add(self, person):
        self._persons.append(person)
        
    def write(self):
        with open(self._file_name,"w") as file:
            for p in self._persons:
                p.write(file)
        

base = Base()

p = Person("John", "Donny", 1995)
base.add(p)

p = Person("Aaa", "Bbbbb", 1990)
base.add(p)



base.print()

base.write()


