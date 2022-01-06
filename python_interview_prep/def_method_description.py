def f(x,y):
    return x+y

z=f(2,3)
print(z)
print(f.__dict__,'\n',"class O/p", f.__class__,"f.__closure__op",f.__closure__,"f.__defaults__" ,f.__defaults__, f.__code__," f.__globals__", f.__globals__, f.__name__)