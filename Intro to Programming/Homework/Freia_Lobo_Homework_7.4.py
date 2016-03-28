#Freia Lobo - fll220@nyu.edu - Homework #7 Problem #4
import random
outfile = open ('numbers.txt','w')
number = int(input("How many numbers do you want "))
outfile = open('numbers.txt','w')
for i in range (1,number+1):
    n = random.randint(1,100)
    outfile.write(str(n)+'\n')
outfile.close()
print('Data written to numbers.text')
