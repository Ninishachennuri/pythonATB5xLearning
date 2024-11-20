for i in range(0, 10, 1): # 0 to 9
    if i == 6 or i == 5:
        print(i)
    else:
        pass # pass is a place holder statement that does nothing
    #It's used when a statement is syntactically required but no action is needed

# | i | condition | o/p
# | 0 | 0 == 6 -> False | o/p - Nothing will be printed
# | 1 | 1 == 6 -> False | o/p - Nothing will be printed
# | 2 | 2 == 6 -> False | o/p - Nothing will be printed
# | 3 | 3 == 6 -> False | o/p - Nothing will be printed
# | 4 | 4 == 6 -> False | o/p - Nothing will be printed
# | 5 | 5 == 5 -> False | o/p - 5
# | 6 | 6 == 5 -> False | o/p - 6
# | 7 | 7 == 6 -> False | o/p - Nothing will be printed
# | 8 | 8 == 6 -> False | o/p - Nothing will be printed
# | 9 | 9 == 6 -> False | o/p - Nothing will be printed
# | 10 | 10 == 6 -> For loop finished


