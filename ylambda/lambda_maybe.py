#!python3.7
# link : https://realpython.com/python-lambda/#alternatives-to-lambdas

print ("\nCase 1.1 with lambda")
print (list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow'])))
print ("Case 1.1 without lambda")
print ([x.capitalize() for x in ['cat', 'dog', 'cow']])


print ("\nCase 2.1 with lambda")
print (list(filter(lambda x: x%2 == 0, range(11))))
print ("Case 2.2 with no lambda")
print ([x for x in range(11) if x%2 == 0])


import functools

print ("\nCase 3.1 with lambda")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0))

print ("Case 3.2 with no lambda")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print (sum(x[0] for x in pairs))

