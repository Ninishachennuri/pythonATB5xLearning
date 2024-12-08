#Web Autmation - Selenium
#page - you are going automate
from dotenv import load_dotenv
import os

class VWOLoginPage():

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_conform(self):
        if self.email == "ninisha@gmail.com" and self.password == "teja123":
            print("Allowed, Login Sucess")

        else:
            print("Login Failed")

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email, password)

VWO_obj = VWOLoginPage(email, password)
VWO_obj.login_conform()

