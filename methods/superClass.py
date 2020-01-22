class Figure(object):
    def __init__(self, one):
        print("Figure init called.")
        self.one = one

    def method(self):
        return self.one

class Circle(Figure):
    def __init__(self, two):
        super().__init__(self)
        print("Circle init called.")
        self.two = two

    def method(self):
        return self.two

my_object = Circle('Jetty')
print(Circle.__mro__)
