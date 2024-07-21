# Write a Python program to check whether an element exists within a tuple.
def check_elemnt(input_tuple,element):
    if element in input_tuple:
        return True
    else:
        return False
Tuple = (1,2,3,4,5)
element_to_check = 3

result = check_elemnt(Tuple, element_to_check)
if result:
    print(f"Element {element_to_check} exits in the tuple.")
else :
     print(f"Element {element_to_check}does not exits in the tuple.")
