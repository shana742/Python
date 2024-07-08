# Swap with temp

def st(a,b):
    print(f"Before swapping: a = {a}, b= {b}")
    temp = a
    a = b
    b = temp
    print(f"After swapping: a = {a}, b = {b}")
    return a, b

x = 10
y = 20
x,y = st(x,y)


#  swap without a temporary varible

def st(a,b):
    print(f"Before swapping: a = {a}, b= {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swapping: a = {a}, b = {b}")

n = 5
t = 10
n ,t = st(n,t)
