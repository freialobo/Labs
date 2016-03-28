#Freia Lobo - fll220@nyu.edu - Homework #7 Problem #2
import math
dataset = [3, 6, 7, 5, 4, 2, 2, 1, 10, 9, 4, 6, 4, 5, 2, 7, 8, 3, 9, 3]
def calculate_standard_deviation(list1):
    total1 = 0
    length = len(list1)
    for i in range (0, length):
                    total1+=(list1[i])
    average = total1/len(list1)
    total2 = 0
    for i in range (0,length):
        total2+=((list1[i]-average)**2)
    stdev =math.sqrt( total2/(length-1))
    return stdev
dataset_stdev = calculate_standard_deviation(dataset)
print ("The standard deviation is ",dataset_stdev)
