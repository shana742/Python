# Write a Python program to check whether a list contains a sub list

def sublist(mainlist,sublist):
    main_tuple = tuple(mainlist)
    sublist_tuple=tuple(sublist)

    for i in range(len(main_list)-len(sublist) +1):
        if main_tuple[i:i+len(sublist)] == sublist_tuple:
            return True
    return False

main_list = [1,2,3,4,5,6,7,8,9]
sublist1=[3,4,5]
sublist2=[8,9,10]

print("Main List:", main_list)
print("Sublist 1:", sublist1)
print("Sublist 2:", sublist2)

print("does main list contain sublist 1 ?",sublist(main_list,sublist1))
print("does main list contain sublist 2 ?",sublist(main_list,sublist2))
