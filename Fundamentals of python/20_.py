# Write a Python function that takes a list of words and returns the length 
# of the longest one




def l(words_list):
    word_len = []
    for n in words_list:
         word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][1]
print(l(["Backend","front", "python","React",]))
