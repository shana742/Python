# Write a Python function that takes two lists and returns true if they have 
# at least one common member

def data(list1 , list2):
   set1 = set(list1)
   set2 = set(list2)

   if set1.intersection(set2):
       return True
   else:
       return False

list1 = [1,2,3,4,5,]
list2 = [5,6,7,8,9]
if data(list1, list2):
    print("list have at least one common member")
else:
    print("list do not have any common member")
