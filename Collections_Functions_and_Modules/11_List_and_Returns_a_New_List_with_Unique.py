#Write a Python function that takes a list and returns a new list with unique 
#elements of the first list

def  l(List):
    l = []

    for i in List:
        if i not in l:
            l.append(i)
    return l
Data = [1,2,2,4,5,4,7,8,8,9,5]
List = l(Data)
print("Original List :", Data)
print("List with unique elemnts:", List)
