#  Write a Python program to find the first appearance of the substring 
#'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
#whole 'not'...'poor' substring with 'good'. Return the resulting string.

def l(string):
    not_index = string.find('not')
    poor =string.find('poor')

    if not_index != -1 and poor != -1 and not_index < poor:
        newstring = string[:not_index] + 'good' + string[poor + len('poor'):]
        return newstring
    else:
        return string

inputstring = "The weather is not that poor today "
resultingstring = l(inputstring)
print(resultingstring)
