#Write a Python program to count the number of strings where the string 
#length is 2 or more and the first and last character are same from a given 
#list of strings.


x=eval(input('enter  a list'))
print(x)
count = 0
for word in x:
    if len(word)>1 and word[0]==word[-1]:
        count=count+1
print('number of that patterns is : ', count)
