    
#method 2
#Write a program that finds the largest of three numbers.
#Can you think of a way to write this program using functions?

n1 = int (input ("Enter the first number "))
n2 = int (input ("Enter the second number "))
n3 = int (input ("Enter the third number "))
if n1 > n2:
    if n1>n3:
        print (n1)
    else: print (n2)
else:
    if n2> n3:
        print (n2)
    else: print (n3)


    
