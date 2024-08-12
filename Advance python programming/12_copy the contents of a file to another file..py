# Write a Python program to copy the contents of a file to another file.

f1=open('create.txt','r')
f2=open('create2.txt','w')
for line in f1:
    f2.write(line)
f1.close()
f2.close()
