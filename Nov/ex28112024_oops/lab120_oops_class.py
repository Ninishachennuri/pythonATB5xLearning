class Person:
    # Attributes - what you have

    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    #behaviour - what you can do

    def talk(self): #NRNG # self - this, self will be first argument in every behaviour.
        print("I can talk")

    def sleep(self, name): #arg with no return
        print("I am a method!!")
        print("sleep", name)

    def sleep2(self, name):  #Arg with return
        print("I am a method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self): #No arg with return
        return "I am walking"


#Create an object of the class
#ObjectRef = classname() -> object
geeta = Person()
geeta.name = "Geeta Sharma"
geeta.gender = "Female"
