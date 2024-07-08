# Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.

a = int(input("Enter First Value : "))
b = int(input("Enter Second Value : "))
c = int(input("Enter Third Value : "))

if a == b or b ==c or c== a:
    print("Sum is : ",0)
else:
    print("Sum is : ",a+b+c)
