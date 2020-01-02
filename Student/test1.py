class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())
