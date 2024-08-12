# How Do You Handle Exceptions With Try/Except/Finally In Python? 
# Explain with coding snippets


# -  Handling exception with try , except and finally in python allows you
#  to mange errors gracefully and ensure that necessary cleanup action are
# performed regardless of whether an error ocured.


def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print(f"Error: cannot divide by zero.({e})")
    else:
        print(f"Divison succesuly Result: {result} ")
    finally:
        print("excution of finally blocj")
divide(10,2)
divide(10,0)
