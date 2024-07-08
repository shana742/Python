#Write a Python program to get a string made of the first 2 and the last 
# 2 chars from a given a string. If the string length is less than 2, return 
# instead of the empty string

def l(text):
    if len(text) < 2:
        return ""
    return text[:2] + text[-2:]

mystring = input("enter a string : ")
print("New string is : ",l(mystring))
