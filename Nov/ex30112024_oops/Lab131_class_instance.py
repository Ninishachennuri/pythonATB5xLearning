class Person:
    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name

ninisha = Person("ninisha")
teja = Person("teja")

print(ninisha.name)
print(teja.name)

print("who is walking", ninisha.walk())
print("who is walking", teja.walk())