# Write a Python program to read a file line by line and store it into a list


with open("create.txt") as f:
    l = f.readlines()
print(l)

l = [x.strip() for x in l ]
print(l)
