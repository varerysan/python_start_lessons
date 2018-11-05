# простой пример небольшой базы даннх людей
import json

class Person:
    def __init__(self, name, surname, birth):
        self._name = name
        self._surname = surname
        self._birth_year = birth
        
    def print(self):
        print("Name:={}=".format(self._name))
        print("Surname:={}=".format( self._surname))
        print("Birth year:={}=".format( self._birth_year))
        
    def write(self, file):
        file.write(self._name + "\n")
        file.write(self._surname + "\n")
        file.write(str(self._birth_year) + "\n")
        
    def read(self, file):
        self._name = file.readline()
        if not self._name:
            return False
        self._surname = file.readline()
        self._birth_year = file.readline()
        return True
    
    @staticmethod
    def read_v2(file):
        name = file.readline().rstrip("\n")
        if not name:
            return None
        surname = file.readline().rstrip("\n")
        birth_year = file.readline().rstrip("\n")
        p = Person(name, surname, birth_year)
        return p
        
        
        

class Base:
    def __init__(self):
        self._persons = []
        self._file_name = "db_persons.dat"
    
    def print(self):
        for p in self._persons:
            print("-" * 30)
            p.print()
        print("-" * 30)

            
    def add(self, person):
        self._persons.append(person)
        
    def write(self):
        with open(self._file_name, "w") as file:
            for p in self._persons:
                p.write(file)

    def read(self):
        self._persons = []
        with open(self._file_name, "r") as file:
            while True:
                p = Person.read_v2(file)
                if p:
                    self._persons.append(p)
                else:
                    break

        
def print_menu():
    print("1. Считать базу из файла")
    print("2. Записать базу в файл")
    print("3. Распечатать базу")
    print("4. Ввести данные")
    print("E. Выход")

base = Base()

#p = Person("John", "Donny", 1995)
#base.add(p)
#
#p = Person("Aaa", "Bbbbb", 1990)
#base.add(p)



while True:
    print_menu()
    case = input("Ваше действие:")

    if case == "1":
        base.read()
    elif case == "2":
        base.write()
    elif case == "3":
        base.print()
    elif case == "4":
        break


