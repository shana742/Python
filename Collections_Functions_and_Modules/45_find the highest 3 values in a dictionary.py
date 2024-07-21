# Write a Python program to find the highest 3 values in a dictionary


def highest(d):
    sorted_items = sorted(d.items(), key = lambda x: x[1], reverse= True)
    highest_value = sorted_items[:3]
    return highest_value

d = {'a':100, 'b':300, 'c':200, 'd':150, 'e':300, 'f':10}

top_three = highest(d)
print("highest 3 value in hthe  dict : ")
for key, value in top_three:
    print(f"{key}: {value}")
