# Write a Python program to test whether a passed letter is a vowel or not

def vowel(letter):
    vowels = ['a','e','i','o','u']
    if letter in vowels:
       return True
    else:
       return False

letter = input("enter a letter : ")

if len(letter) == 1 and letter.isalpha():
    if vowel(letter):
        print(f"The letter'{letter}' is a vowel")
    else:
        print(f"The letter '{letter}' is not a vowel")
else:
    print("Please enter a single alphbet cahrecter")
