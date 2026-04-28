class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programee(Employee):
    def __init__(self,name, id , lang):
        super().__init__(name , id)
        self.lang = lang

rohan = Employee("Rohan Das" , "420")
harry = Programee("Harry" , "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)