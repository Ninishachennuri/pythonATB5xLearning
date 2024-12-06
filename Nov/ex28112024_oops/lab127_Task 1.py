#Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods

class pyATB:
    Name = None
    Age = None
    city = None
    exp = None
    company = None


    def __init__(self, Name, Age, city, exp, company):
        self.Name = Name
        self.age = Age
        self.city = city
        self.exp = exp
        self.company = company

    def Student_info(self):
        print(f"Student Name: {self.Name}", f"Age is: {self.age}", f"city is :{self.city}", f"experience is: {self.exp}",
              f"Company is: {self.company}")



s1 = pyATB("Ninisha", 25, "Hyderabad", "5", "tcs")
s2 = pyATB("Swathi", 35, "Newdelhi", "12", "uts")
s3 = pyATB("sreelatha", 32, 5, "10", "accenture")

s1.Student_info()
s2.Student_info()
s3.Student_info()