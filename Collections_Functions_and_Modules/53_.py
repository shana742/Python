#  How can you pick a random item from a list or tuple?

# -> using random.choice




import random
my_list = [1, 2, 3, 4, 5]
random_item_from_list = random.choice(my_list)
print(f"Random item from list: {random_item_from_list}")

my_tuple = ('apple', 'banana', 'cherry')
random_item_from_tuple = random.choice(my_tuple)
print(f"Random item from tuple: {random_item_from_tuple}")
