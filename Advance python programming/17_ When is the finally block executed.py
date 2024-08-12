# When is the finally block executed?

# - it runs after the try block and after the 'except' block or after
#    the else block

def fun():
    try :
         print("trying the excute")
         result = 10/2
    except ZeroDivisioError:
         print("Caught division by zero ")
    else:
         print("No exception occured.")
    finally:
         print("this block is alwys excuted")
fun()

    



