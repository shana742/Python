#  Write a Python program to read last n lines of a file


def last(fname, n):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end = '')
if __name__ == '__main__':
    fname = 'create.txt'
    n = 1
    try:
        last(fname,n)
    except:
        print('file not found')
