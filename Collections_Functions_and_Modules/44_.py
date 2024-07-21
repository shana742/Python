# Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary.
#Sample data: {'1': ['a','b'], '2': ['c','d']} 
#Expected Output:
#ac ad bc bd


from itertools import product

def combine(d):
    combination = [''.join(comb) for comb in product(*[d[key] for key in d])]
    return combination

data = {'1': ['a','b'], '2': ['c','d']}

combination = combine(data)
print("combination:",combination)
