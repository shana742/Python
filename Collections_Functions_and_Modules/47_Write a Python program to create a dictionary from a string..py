#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. 
#Sample string: 'w3resource'
#Expected output:
#{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


def count_letters(string):
    letter_counts = {}
    for char in string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts

sample_string = 'w3resource'
result = count_letters(sample_string)
print(result)
