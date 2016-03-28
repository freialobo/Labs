#Freia Lobo - fll220@nyu.edu - Homework #4 Problem #2

def eligibility(age,years):
    if (age >= 30) and (years>=9):
        verdict = "House and Senate" #If a person is eligible for Senate he is automatically eligible for house as well
        return verdict #This is because the elibility for House is a subset of the eligibility for Senate
    elif (age >=25) and (years>=7):
            verdict = "House"
            return verdict
    else:
        verdict = "None"
        return verdict
blue = int (input("What is your age? "))
green = int (input ("How many years have you been a US citizen? "))
verdict = eligibility (blue, green)
print ("You are eligible for", verdict)
