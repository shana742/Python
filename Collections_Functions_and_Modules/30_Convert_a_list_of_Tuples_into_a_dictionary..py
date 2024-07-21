# Write a Python program to convert a list of tuples into a dictionary.

l = [("a", 1),("a",2),("b",1),("b",2),("c",1)]

d ={}
for a,b in l:
    d.setdefault(a,[]).append(b)

print(d)
print(type(d))
