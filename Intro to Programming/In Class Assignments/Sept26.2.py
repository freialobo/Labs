#Write a program that finds the largest of three numbers.
#Can you think of a way to write this program using functions?

def find_greatest_number():
    n1 = int (input ("Enter the first number "))
    n2 = int (input ("Enter the second number "))
    n3 = int (input ("Enter the third number "))
    if n1 > n2:
              greatest = n1
    else:
        greatest = n2
        if n3 > greatest:
                  greatest = n3
    return greatest
greatest = find_greatest_number()
print ("The greatest number is ", greatest)
                  
              

