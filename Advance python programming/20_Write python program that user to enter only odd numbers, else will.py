# Write python program that user to enter only odd numbers, else will
# raise an exception.


def oddnum():
    while True:
        try:
            userinput =input("enter odd num : ")
            num = int(userinput)
            if num %2 == 0:
                raise ValueError("the number is not odd")
            print("you entered an odd number :",num)
            return num
        except ValueError as e:
            print("Error: Please try again.",e)
oddnum()
