class X:
    pass

class Y(X):
    pass


class Z(X,Y):
    pass

print(Z.__mro__)