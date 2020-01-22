class Figure(object):
    def __init__(self, one):
        print("Figure init called.")
        self.one = one

    def method(self):
        return self.one


class Circle(Figure):
    def __init__(self, two):
        Figure.__init__(self, two)
        print("Circle init called.")
        self.two = two


# class inheritance
my_draw = Circle('Tor')
print(my_draw.one)
print(my_draw.two)
print(my_draw.method())
print(Circle.__mro__)
