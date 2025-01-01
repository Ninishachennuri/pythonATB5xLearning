print("---Start the program")
try:
    a = int(input("Ent the num1")) # ValueError: invalid literal for int() with base 10: 'pramod'
    b = int(input("Ent the num2"))
    c = a / b # ZeroDivisionerror: division by zero
    print("Result Div is ", c)
except Exception as e:
    print(e)

print("---End of the program")

#try and expect