# Match Statement -> Switch in Java
#match the op and execute
#python > 3.10

#match variable:
#    case pattern1:
#         # code block
#    case pattern2:
#         # code block

# Write a program to ask the user which browser he want to run automation

browser_name = input("enter the browser name\n")
match browser_name:
    case "fire fox":
        print("Starting firefox")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser Not Found")
