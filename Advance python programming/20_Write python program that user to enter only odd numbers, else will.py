# Write python program that user to enter only odd numbers, else will
# raise an exception.


def oddnum():
    while True:
        try:
            userinput =input("enter odd num")
            num = int(userinput)
            if num %2 == 0:
                raise ValueError("the number is not odd")
            print(f"you entered an odd number : {num}")
            return num
        except ValueError as e:
            print(f"Error: {e}.Please try again.")
oddnum()
