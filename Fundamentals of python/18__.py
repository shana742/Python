#Write a Python program to add 'ing' at the end of a given string (length 
#should be at least 3). If the given string already ends with 'ing' then add 
#'ly' instead if the string length of the given string is less than 3, leave it 
#unchanged


def l(string):
    if len(string) < 3:
        return string
    elif string.endswith("ing"):
        return string + "ly"
    else:
        return string + "ing"
    
test_string = ["play", "playing","go","run"]

for s in test_string:
    result = l(s)
    print(f"original:{s}, Modified:{result}")

