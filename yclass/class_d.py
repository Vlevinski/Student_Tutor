class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def double_sum(self):
        return 2 * self.x + 2 * self.y

class B(A):
    def __init__(self, x):
        super(B, self).__init__(x, x)

class C(B):
    def __init__(self,y):
        super(C, self).__init__(y)


a = A(2,3)
print(a.multiply())

b = B(5)
print (b.multiply(), b.double_sum())

c= C(7)
print(c.multiply(), c.double_sum())

'''
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
'''
