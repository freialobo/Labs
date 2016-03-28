#Freia Lobo - Homework #5 - Problem #1

budget = int( input ("Enter your budget for the month in $ "))
answer = "y"#setting the original value to "y" so that the loop runs the first time
total = 0 #defining the variable 
while (answer == "y"):
    expense = int (input ("Enter your expense in $ "))
    total += expense
    answer = input ("do you have another expense to enter? enter y if yes and n if no " )
difference = budget - total
if difference>0:
    print ("You are under budget by $", difference)
elif difference<0:
    print ("You are over budget by $", difference*(-1))#because difference will be -ve
else:
    print ("You have spent as per your budget")
    

