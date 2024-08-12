#  Write a Python program to read a file line by line store it into a variable


def file(fname):
    with open(fname, 'r') as myfile:
        data=myfile.readlines()
        print(data)
file('create.txt')
