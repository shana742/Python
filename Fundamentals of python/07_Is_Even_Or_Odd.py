# Write a Python program to find whether a given number is even or odd, 
# print out an appropriate message to the user


def Check_even_odd(number):
    if number % 2== 0:
        print(f"The Number {number} is even")
    else:
        print(f"The number{number} is odd")

number = int(input("Enter a number: "))
Check_even_odd(number)
