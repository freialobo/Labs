#Freia Lobo - fll220@nyu.edu - Homework #5 Problem #2
def color_result():
        if c1 == "blue":
            if  c2 == "red":
                    print ("result:purple")
            elif c2 == "yellow":
                    print("result:green")
            elif c2 == "blue":
                    print ("result: blue")
            
        elif c1 == "yellow":
             if  c2 == "red":
                     print ("result:orange")
             elif c2 == "blue":
                    print("result:green")
             elif c2 == "yellow":
                    print ("result: yellow")
                
        elif c1 == "red":
                if  c2 == "red":
                        print ("result:red")
                elif c2 == "yellow":
                    print("result:orange")
                elif c2 == "blue":
                    print ("result: purple")
condition1 = False
condition2 = False
while condition1 == False:
        c1 = input("Enter the name the first valid primary color ").lower() #This is in anticipation of users typing uppercase letters which would not agree with the program
        if c1 == "blue" or c1 == "yellow" or c1 == "red":
                condition1 = True
while condition2 == False:
        c2 = input("Enter the name of the second valid a primary color ").lower() #This is in anticipation of users typing uppercase letters which would not agree with the program
        if c2 == "blue" or c2 == "yellow" or c2 == "red":
                condition2 = True

color_result()


