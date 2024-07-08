#  Write a Python program to count occurrences of a substring in a string
 


string = input("enter a String: ")
substring = input("enter a substring : ")

count = string.count(substring)
print("substring occurs %d times " % count)
