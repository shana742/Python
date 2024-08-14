# Write a Python program to read a file line by line and store it into a list

l = open('create.txt','r')
lines = l.readlines()
lines = [line.strip() for line in lines]
print(lines)
