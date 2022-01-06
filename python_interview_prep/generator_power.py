def powTwo(max=0):
    n=0
    while n<max:
        yield n
        n=n+1


a=powTwo(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))