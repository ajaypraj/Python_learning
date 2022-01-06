def add():
    return "say hi"

def decor(func):
    def inner():
        return func().upper()
    return inner

@decor
def add():
    return "say hi"

print(add())





