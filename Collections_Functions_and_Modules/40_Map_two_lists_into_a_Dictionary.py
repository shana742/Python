#  Write a Python program to map two lists into a dictionary

def list_dict(keys,values):
    if len(keys) != len(values):
        raise ValueError("The two list must have the same length.")

    mapped_dict = dict(zip(keys,values))
    return mapped_dict

keys_list = ["name","age","city"]
value_list=["alice",25,"New york"]

result_dict = list_dict(keys_list, value_list)

print("mapped Dictionary:" , result_dict)
