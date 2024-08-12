# Write a Python program to write a list to a file.

l = ["python",'java','js','saas','css','html']
print(l)
filename = open('create.txt','w')
content = '\n'.join(l)
filename.writelines(content)
