#  Write a Python program to read a file line by line store it into a variable


l = open('create.txt','r')
line1 = l.readline().strip()
line2 = l.readline().strip()
line3 = l.readline().strip()

print('line1  :',line1)
print('line2  :',line2)
print('line3  :',line3)
