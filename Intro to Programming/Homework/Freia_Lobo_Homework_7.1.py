#Freia Lobo - fll220@nyu.edu - Homework #7 Problem #1
import random
n1 = random.randint(1,100)
guess = 0
count = 0
guess = int(input("Guess a number between 1 and 100  "))
while guess!=n1:
    if guess >n1:
        print ("Lower!")
    elif guess < n1:
        print ("Higher!")
    count+=1
    guess = int(input("Guess a number between 1 and 100  "))
print ("You have guessed the right, the number is ", n1)
print ("It took you", count, "guesses to get it right")
        
