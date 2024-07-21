# Write a Python program to replace last value of tuples in a lis

l = [(10,20,30),(40,50,60),(70,80,90)]
print(l)
print([t[:-1]+(100,) for t in l])
