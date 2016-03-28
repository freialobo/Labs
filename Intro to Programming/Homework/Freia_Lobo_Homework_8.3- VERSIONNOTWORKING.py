#Freia Lobo - fll220@nyu.edu - Homework #8 Problem #3
#Using Bubble Sort 
def print_top_scores(list1,n):
    sort = False
    while sort == False:
        for i in range(len(list1)-1):
            if list1[i][1]<list1[i+1][1]:
                sort = False
                list1[i],list1[i+1]=list1[i+1],list1[i]
                print(list1)
