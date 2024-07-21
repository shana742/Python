# Write a Python program to print all unique values in a dictionary.


def unique_dict(d):
    unique_values = set()

    for value in d.values():
        unique_values.add(value)
    return unique_values

d =  {'a': 100, 'b': 200, 'c':300, 'e': 100,'d':200}

unique_values = unique_dict(d)

print("unique values in the dict:", unique_values)
