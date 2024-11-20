# Problem find the max between 3 numbers

#Logic building

#user inputs num1, num2, num3 -> int
#o/p -> int or string with max number

#logic ? if else -> 1 condition

#syntax
#if condition 1:
#    print("do 1")
#elif condition 2:
#    print("do 2):
#elif condition 3:
#    print("do 3")
#else
#    print("do for else")

num1 = int(input("Enter the num1\n")) #5 , #10
num2 = int(input("Enter the num2\n")) #3 , #12
num3 = int(input("Enter the num3\n")) #2 , #11

# 5 > 3 and 5 > 2 -> 5
# num1 > num2 and num2 > num3 -> num2

# 12 > 10 and 12 > 11 -> true -> 12
#num2 > num1 and num2 > num3 -> num3

#num3

if num1 > num2 and num1 > num3:
    print("Max is ", num1)

elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else:
    print("Max is", num3)