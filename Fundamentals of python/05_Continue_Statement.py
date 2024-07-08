# What is the purpose continue statement in python?

# -> The continue statement in python  is used within loops to skip the rest of the code inside
#     the loop for the current iteration and proceed to the next iteration.


for num in range(10):
    if num % 2 == 0:
        continue
    print(f"Odd number : {num}")
