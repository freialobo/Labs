#Freia Lobo - fll220@nyu.edu - Homework #5 Problem #3
n1 = 37 #let this be the number. at a later stage this can be modified to be a randomly generate number
guess = 0
count = 0
while guess!=n1:
    if guess >n1:
        print ("Lower!")
    elif guess < n1:
        print ("Higher!")
    count+=1
    guess = int(input("Guess a number between 1 and 100  "))
print ("You have guessed the right number!")
print ("It took you", count, " guesses to get it right")
        
