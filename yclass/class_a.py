#! python3.7
#

import math


class Ring(object):
    """ Here is the modified Python language class"""

    def __init__(self, *kw):
        # init is the initializer which initialize the instance variable
        self.date, self.metal, self.radius, self.price, self.quantity = kw

    def cost(self):
        # the cost
        return self.price * self.quantity

    def area(self):
        # the area
        return math.pi * self.radius ** 2

    def value(self):
        print("Date: ", self.date, "metal: ", self.metal, "cost: ", self.cost(), "area: ", round(self.area(), 2))


'''
r = Ring("2017=08-10", "Gold", 5.5, 10.5, 10)
'''
