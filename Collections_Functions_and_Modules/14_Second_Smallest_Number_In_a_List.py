# Write a Python program to find the second smallest number in a list
def second(numbers):
    if len(numbers)<2:
       return None

    smallest = float('inf')
    second = float('inf')
    for num in numbers:
       if num<smallest:
           second = smallest
           smallest = num
       elif num < second and num != smallest:
           second = num
    return second

List = [12,3,4,6,9,10,]
result = second(List)
print("second smallest number:",result)
                      
