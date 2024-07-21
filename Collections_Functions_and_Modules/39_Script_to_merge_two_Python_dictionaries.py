# Write a Python script to merge two Python dictionaries


def merge_dicts(dict1, dict2):
    merge_dict = {**dict1, **dict2}
    return merge_dict

dict1 = {'1':1, 'b':2}
dict2 = {'c':3, 'd':4}

merge_dict = merge_dicts(dict1,dict2)
print("merged dictionary : ", merge_dict)
