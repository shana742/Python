# Write a Python program to write a list to a file.

l = ["python",'java','js','saas','css','html']
print(l)
fname = open('create.txt','w')
for item in l:
    fname.write(item + '\n')
