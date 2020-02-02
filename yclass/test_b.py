#!python3.7
#

from yclass import class_b

r = class_b.Ring("2017=08-10", "Gold", 5.5, 10.5, 10)
print(r.date, r.metal, r.radius, r.price, r.quantity)
