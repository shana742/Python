# Write a Python program to check multiple keys exists in a dictionary

def check_key(dict,keys):

    for key in keys:
        if key not in dict:
            return False
    return True

my_dict = {'a':1,'b':2,'c':3}
keys_check = ['a','b','d']
result = check_key(my_dict,keys_check)
print(f"all keys exits:{result}")

keys_check = ['a','b','c']
result = check_key(my_dict,keys_check)
print(f"all keys exits:{result}")

