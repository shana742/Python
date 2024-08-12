# Write a python program to find the longest words

f = open('create.txt','r')
s=f.read()
lst=s.split()
print(max(lst,key=len))
