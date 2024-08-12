# When will the else part of try-except-else be executed?

# - the else part of try-except-else blocks is excuted when the code
#inside the 'try' block runs without raising any exception.

try :
    result = 10/2
except zerodivsioError:
    print("cannot divide ")
else:
    print("division succesfully",result)


