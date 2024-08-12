# Write a Python program to count the number of lines in a text file.

f = open("create.txt","r")
lst = f.readlines()
print("lines are :",len(lst))
f.close()
