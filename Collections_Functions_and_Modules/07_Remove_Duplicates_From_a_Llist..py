# • Write a Python program to remove duplicates from a list.

l = [10,20,20,30,40,40,50,50,50,70]

def remove(duplist):
    c = []

    for i in duplist:
        if i not in c:
            c.append(i)
    return c
print(remove(l))
