#Web Autmation - Selenium
#page - you are going automate

class VWOLoginPage():

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_conform(self):
        if self.email == "ninisha@gmail.com" and self.password == "teja123":
            print("Allowed, Login Sucess")

        else:
            print("Login Failed")

#email = Read from test data - Excel, CSV or ENV file
#password = Read from test data - Excel.CSV or ENV file

#VWO_obj = VWOLoginPage(email, password)
#VWO_obj.login_conform()

ninisha = VWOLoginPage("ninisha@gmail.com", "teja123")
ninisha.login_conform()