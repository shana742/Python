#  Write a Python program to combine two dictionary adding values for 
# common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

from collections import Counter

def combine(d1, d2):
    combine = Counter()
    combine.update(d1)
    combine.update(d2)
    return combine

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}

combine_dict = combine(d1,d2)
print("Combined Dictionary:", combine_dict)




