# Write a Python function to check whether a number is in a given range

def is_in_range(number, start, end):
    return start <= number <= end


print(is_in_range(5, 1, 10))  
print(is_in_range(15, 1, 10))
