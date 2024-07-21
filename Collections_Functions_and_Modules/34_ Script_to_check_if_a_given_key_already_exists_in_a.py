#  Write a Python script to check if a given key already exists in a 
# dictionary.


d = {1:10,2:20,3:30,4:40,5:50,6:60}

def keypresent(x):
    if x in d:
        print('key is present in the dictonary')
    else:
        print('key is not present in the dictoinary')
keypresent(2)

