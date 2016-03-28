#Freia Lobo - Homework #8 Problem #4
#Selection Sort
sourcelist = [4,8,1,3,2,9,5,7,6]
def selection_sort(list1):
    for i in range (len(list1)):
                listmin = min(list1[i:])
                listmin_index = list1[i:].index(listmin)
                list1[i+listmin_index] = list1[i]
                list1[i] = listmin
    return list1
output = selection_sort(sourcelist)
print(output)
