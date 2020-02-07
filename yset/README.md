# Sets in Python

Propeties of set:
- unordered
- unique elements
- modified elements
- immutable types ( NO list, No dict) Yes tuple

Declaration:
    x = set(<iter >)  or x = {<obj>, <obj>, ..., <obj>}

*x = {42, 'foo', (1, 2, 3), 3.14159}*

Operations:
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

union : a.union(b, c, d)   or a | b | c | d
intersection : a.intersection(b, c, d) or a & b & c & d
difference : a.difference(b, c) or a - b - c
simmetric diffence: a.symmetric_difference(b, c)   or  a ^ b ^ c
common elements : a.symmetric_difference(b, c)
subset : x1.issubset(x2)   or x1 < x2
superset x1.issuperset(x2)  or x1 >= x2

modifying:

x1.update(x2, x3 ...])  or x1 |= x2 | x3 ...]
x1.intersection_update(x2, x3 ...]) or x1 &= x2 & x3 ...]
x1.difference_update(x2, x3 ...]) or x1 -= x2 | x3 ...]
x1.symmetric_difference_update(x2) or x1 ^= x2

other methods:

x.add(<elem>)
x.remove(<elem>)
x.discard(<elem>)
x.pop()
x.clear()

Frozen set - immutable

x = frozenset({1, 2, 3})
y = frozenset({'a', 'b', 'c'})
d = {x: 'foo', y: 'bar'}
print (d)
{frozenset({1, 2, 3}): 'foo', frozenset({'c', 'a', 'b'}): 'bar'}
