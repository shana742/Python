# Write a Python program to count the occurrences of each word in a
# given sentencs

def count (str):
    l = {}
    w = str.split()

    for i in w:

        if i in l:
            l[i]+=1
        else:
            l[i]=1
    return l

syntax = input("enter a sentence : ")
print(count(syntax))
