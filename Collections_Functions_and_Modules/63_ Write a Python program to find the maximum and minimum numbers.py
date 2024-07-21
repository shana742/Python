#  Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers

def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num

decimal_numbers = [120, 300, 200, 400, 600, 10,20]

max_num, min_num = find_max_min(decimal_numbers)
print(f'The maximum number is {max_num}')
print(f'The minimum number is {min_num}')

