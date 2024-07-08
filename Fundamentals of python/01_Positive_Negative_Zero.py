def CheckNumber(num):
    if num > 0 :
        print( "the Number Is Positive")
    elif num < 0 :
        print( "the Number Is Negative")
    else:
        print( "the Number Is zero")

num = float(input("Enter A Number : " ))

print(CheckNumber(num))
