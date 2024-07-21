# Write a Python function that checks whether a passed string is 
#palindrome or no


def is_palindrome(s):
    cleaned_str = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_str == cleaned_str[::-1]


print(is_palindrome("A man, a plan, a canal, Panama"))  
print(is_palindrome("racecar"))                       
print(is_palindrome("hello"))                         
