# Write a Python program to append text to a file and display the text.

f = open('create.txt','a')
str = input(" Enter data to append in create.txt : ")
f.write(str)
f = open("create.txt","r")
print(f.read())
f.close()
