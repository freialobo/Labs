#Freia Lobo - fll220@nyu.edu - Homework #6 Problem #2
a = 0
b = 1
print (a)
print (b)
for i in range (998): #since we already printed the first two numbers
    c = a+b
    print (c)
    a = b
    b = c
    
