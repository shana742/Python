#  Why Do You Use the Zip () Method in Python
# -> in zip() function is used to combin multipke iterables elements-wise into
#     tuples.


# EX:->

keys = ['a','b','c']
values = [1,2,3]
combined = zip(keys, values)
for pair in combined:
     print(pair)
