#Freia Lobo - fll220@nyu.edu - Homework #3 Problem #2
def tax_calculator():
    pretax = float (input ("Enter the price of the purchase in dollars "))
    postax = pretax + (0.08875*pretax)
    return postax
postax = tax_calculator()
print ("The value after tax is ", "%0.2f"%postax)
