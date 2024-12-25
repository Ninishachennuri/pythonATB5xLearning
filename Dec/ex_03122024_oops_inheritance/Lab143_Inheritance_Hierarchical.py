#Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1BHK")

class Pramod(Father):
    def BHK2(self):
        print("2BHK")

class Amit(Father):
    def BHK3(self):
        print("3BHK")

class Lucky(Father):
    def no_house(self):
        print("no_house")

pramod = Pramod()
pramod.BHK1()
pramod.BHK2()

Amit = Amit()
Amit.BHK1()
Amit.BHK3()
#Amit.BHK2 #This belong to pramod

l = Lucky()
l.BHK1() #only father house
