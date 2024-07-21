# How will you compare two lists


a = [1,2,4,1,5,6,7,8,9,10]
b = [2, 1,5,3,6,0,55,9,10]

c = []
for num in a:
     if num in b :
         if num not in c :
             c.append(num)
print(c)
