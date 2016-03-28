#A function to get and return the weight
def get_weight ():
    weight = float (input (" What is your weight in pounds "))
    return weight

#A function to get and return the height
def get_height ():
    height = float (input ("What is your height in inches "))
    return height

#A function to calculate BMI
def calculate_bmi() :
 
    bmi = ((weight*703)/height)
    return bmi

#A function to take and print BMI
def  print_bmi():
        print ("Your BMI is ", bmi)

#Tis is the actual program
        
        
weight = get_weight()
height = get_height()
bmi = calculate_bmi()
print_bmi()
