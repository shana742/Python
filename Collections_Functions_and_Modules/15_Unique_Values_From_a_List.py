#Write a Python program to get unique values from a list

list= [1,4,5,3,2,3,4,5,4,6,6,6]
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)
