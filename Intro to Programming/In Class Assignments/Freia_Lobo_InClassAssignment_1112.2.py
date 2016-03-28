#Freia Lobo - In  Class Assignment - Bubble Sort 
def bubble_sort(list1):
    sort = False
    while sort == False:
        for i in range(len(list1)-1):
            if list1[i]>list1[i+1]:
                    sort = False 
                    list1[i],list1[i+1] = list1[i+1],list1[i]
                    print(list1)
    print(list1)
list1 = [5,4,3,2,1]
bubble_sort(list1)

    
