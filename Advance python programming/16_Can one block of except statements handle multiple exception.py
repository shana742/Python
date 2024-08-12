# Can one block of except statements handle multiple exception?

# - Yes a single 'exept' block can handle multiple exception by specifying a
#   tuple of exception types. this helps to handle multiple exception with
#    the same block of code

try:
    num = int("abc")
    result = 10/0
except(ValueError, ZeroDivisionError) as e:
    print(f"An error occured:{e}")
