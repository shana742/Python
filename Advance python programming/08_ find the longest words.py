# Write a python program to find the longest words

l = open('create.txt','r')
word=l.read().split()
lgw=max(word, key=len)
print('The longest word is :',lgw)
