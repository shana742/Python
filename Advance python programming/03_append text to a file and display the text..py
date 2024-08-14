# Write a Python program to append text to a file and display the text.

f = open('create.txt','a')
str = input(" enter text to apeend : ")
f.write(str)
f = open("create.txt","r")
print(f.read())
f.close()
