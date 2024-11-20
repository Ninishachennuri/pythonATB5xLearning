s1 = int(input("Enter the side 1: \n"))
s2 = int(input("Enter the side 2: \n"))
s3 = int(input("Enter the side 3: \n"))

if s1 == s2 and s1 ==s3 and s2 == s3:
    print("Trial is Equilateral")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("Triangle is isoseles")
else:
    print("Triangle is scalene")