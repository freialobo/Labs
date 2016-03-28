#Freia Lobo - fll220@nyu.edu - Homework #4, Problem #3
def multiple_of_3_5_7(n):
    if(n%105 == 0): #105 is 3*5*7. All multiples of all 3 must be multiples of 105
        answer = True
        return answer
    else:
        answer = False
        return answer
n = int(input("Enter a number to check whether it is a multiple of 3,5 and 7 "))
answer = multiple_of_3_5_7(n)
print (answer)
