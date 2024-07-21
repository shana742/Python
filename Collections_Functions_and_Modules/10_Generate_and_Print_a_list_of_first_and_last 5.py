# Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30.

def l(start , end ):
    squrelist=[x**2 for x in range(start, end +1)]
    return squrelist

squares = l(1,30)
print("First 5 elements:",squares[:5])
print("Last 5 elements:",squares[-5:])
