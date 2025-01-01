import os

print(os.getcwd())
#return the current working directory

#list files in the curent directory
files = os.listdir('/Users/Dr.Teja/PycharmProjects/PyATB5xLearning')
print(f"files in current directory: {files}")

#create a new directory
#os.mkdir('Test2')

#check if a file exists
file_exist = os.path.exists("pramod.txt")
print(file_exist)

print(os.name) # posix == mac, nt - windows