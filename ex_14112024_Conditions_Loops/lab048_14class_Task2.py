#leap day occurs in year that is multiple of 4, except for years evenly divisible by 100 but not by 400

year = int(input("Enter the year"))

if year % 4 == 0 and year % 400 != 100:
    print("is a leap year")
elif year % 100 != 0:
    print("its not leap year")
else:
    print("Enter a valid year")