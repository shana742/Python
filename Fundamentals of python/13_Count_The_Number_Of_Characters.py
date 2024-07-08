#Write a Python program to count the number of characters (character 
# frequency) in a string


string = input("Enter The String : " )
count = {}
for letter in string:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print("count Frequency is ")
for key, value in count.items():
    print(f"{key} occurs {value} times")
