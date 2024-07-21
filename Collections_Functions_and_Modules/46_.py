#Write a Python program to combine values in python list of dictionaries. 
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
#300}, o {'item': 'item1', 'amount': 750}]
#Expected Output:
#Counter ({'item1': 1150, 'item2': 300})

from collections import Counter
def combine(list_dict):
    combine_counter = Counter()

    for d in list_dict:
        for key, value in d.items():
            if isinstance(value,(int,float)):
                combine_counter[key] += value
        return combine_counter

data = [{'item': 750}, {'item2':300}, {'item1': 400} , {'item2': 0}]
combine_values = combine(data)
print(combine_values)

