#Freia Lobo - fll220@nyu.edu - Homework #4 Problem #1

c1 = input("Enter the name of a primary color ").lower() #This is in anticipation of users typing uppercase letters which would not agree with the program
c2 = input("Enter the name of the second primary color ").lower()
if c1 == "blue":
    if  c2 == "red":
                print ("result:purple")
    else:
                if c2 == "yellow":
                    print("result:green")

elif c1 == "yellow":
     if c2 == "red":
                print("result:orange")
     else:
        if c2 == "blue":
                                print("result:green")
elif c1 == "red":
                    if c2 == "blue":
                        print("result:purple")
                    else:
                        if c2 == "yellow":
                             print ("result:orange")
else:
    print ("You have entered an invalid colour")
