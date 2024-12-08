class bank:
    def _init_(self, account_number, balance):
        self.balance = balance # public
        self._account_number = account_number #private

    def check_balance(self):
        print("check_balance")

    def deposite(self,amount):
        self.balance = self.balance + amount

    def public_function(self):
        self.__internal_private_function();

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)

        else:
            print("not allowed!")

    def __internal_private_method(self):
        print("private method, can be access only class")


icici = bank(9876543210, 100)
icici.deposit(100)
icici.check_balance()
print(icici.balance)
# print(icici.__account_number)
icici.show_me_account_number(False)
# icici.__internal_private_method()



