for i in range(0, 10): # 0 to 9, times ->
    if i == 5:
        print("Five")
    else:
        print(i)

# |i | condition | o/p
# |0 | 0 == 5 -> False | o/p = 0
# |1 | 1 == 5 -> False | o/p = 1
# |2 | 2 == 5 -> False | o/p = 2
# |3 | 3 == 5 -> False | o/p = 3
# |4 | 4 == 5 -> False | o/p = 4
# |5 | 5 == 5 -> False | o/p = Five
# |6 | 6 == 5 -> False | o/p = 6
# |9 | 9 == 5 -> False | o/p = 9
# |10 | 10 == 5 -> False | For loop finished - o/p = Exit