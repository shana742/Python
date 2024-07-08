#Write a Python function to insert a string in the middle of a string.


def l(str,word):
    return str[:2] + word + str[2:]
print(l('[[]]','python',))
