

def multiply_by_decor(num):
    def multiply_decor(func):
        def inner(x,y):
            return func(x,y)*num
        return inner
    return multiply_decor

@multiply_by_decor(3)
def add(x,y):
    return x+y

print(add(10,2))