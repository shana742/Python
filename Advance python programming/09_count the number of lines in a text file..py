# Write a Python program to count the number of lines in a text file.


l = open("create.txt","r")
count = l.readlines()
print("lines are :",len(count))

