#Encapsulation
#Hide the data member(class variables, instance variable)
#by using only the methods

class car:
    def __init__(self):
        self.password = "ninisha" #public instance variable
        self._password_secure = "teja123" #private instance variable

    def change_password(self):
        self.__password_secure = "456"

object_ref  = car()
print(object_ref.change_password)
object_ref.change_password()
print(object_ref._password_secure) # 'car' object has no attribute '_password_secre'
