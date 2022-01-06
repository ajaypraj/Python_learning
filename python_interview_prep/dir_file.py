"https://docs.python.org/3/reference/index.html"

class SuperClass:
    list_data = [11,20]
    def hello(self):
        self.name='supper'
        self.data=[1,2]

class Subclass:
    l2=[10]
    def __init__(self):
        self.name="Dinesh"
    def world(self):
        self.age=12


s1=SuperClass()
c1=Subclass()
#print(dir(s1))
#print(dir(c1))
print(f"This is subclass attributes {dir(Subclass)}")
print(c1.__dict__)
c1.__dict__["Vishakaha"]="Hi I am Vishakaha"
print(c1.__dict__)
print(c1.__dict__.values())
print(c1.world.__self__)
print(c1)

