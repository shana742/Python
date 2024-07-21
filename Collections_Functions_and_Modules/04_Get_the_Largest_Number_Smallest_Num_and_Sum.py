# Write a Python function to get the largest number, smallest num and sum 
# of all from a list

def l(numbers):
    if not numbers:
      return None, None, 0
    largest = numbers [0]
    smallest = numbers [0]
    totalSum = 0

    for num in numbers:
        if num > largest :
            largest = num
        if num < smallest:
          smallest = num
        totalSum += num

    return largest, smallest, totalSum

l1=[2, 33, 222,14,25]
largest,smallest,totalSum = l(l1)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of Total number: {totalSum}")


