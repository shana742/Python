# Write a Python program to read first n lines of a file

n = (int(input("enter list to read : ")))
f = open("create.txt")
for i in range(n):
    print(f.readline())
