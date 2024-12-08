class facebook:

    def __init__(self):
        self.public_var = "user"
        self.__private_var = "stranger"

    def usermom(self):
        print(self.__private_var)
        self.__userfather()

    def __userfather(self):
        print("private password")

object_ref = facebook()
object_ref.usermom()
print(object_ref.public_var)