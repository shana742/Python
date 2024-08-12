# Write a Python program to count the frequency of words in a file

f = open('create.txt','r')
wrd=input("enter the word  to serced ")
s=f.read()
lst=s.split()
count = 0
for i in lst:
    if(i==wrd):
        count+=1
print("word {} occured {} Times".format(wrd,count))
