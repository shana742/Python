# Write a Python program to count the frequency of words in a file

from collections  import Counter
l = open('create.txt','r')
s = l.read().split()
wc = Counter(s)
for word,count in wc.items():
    print(f"frequency word: {word} : {count} ")
    

