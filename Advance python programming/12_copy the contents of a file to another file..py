# Write a Python program to copy the contents of a file to another file.


l1=open('create.txt','r')
l2=open('create2.txt','w')
for line in l1:
    l2.write(line)

