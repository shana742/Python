# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

def l(s1,s2):
    if len(s1) <2 or len(s2) <2:
        return " both string must have at least two charcters."

    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]

    result = new_s1 + " " + new_s2
    return result

string1 = "hello"
string2 = "world"

swapped_string = l(string1,string2)
print(swapped_string)
