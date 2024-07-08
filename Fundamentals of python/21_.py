# Write a Python function to reverses a string if its length is a multiple of 4.

def l(data):
    if len(data) % 4 == 0:
        return data[::-1]
    return data

text = input("Enter String : ")
result = l(text)
print("Final String is : ", result)
