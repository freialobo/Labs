#Freia Lobo, fll220@nyu.edu, Homework #3 Problem #3
def calculate_distance():
    velocity = int(input ("How fast were you travelling? (in miles/hour) " ))
    hours = int (input ("For how long were travelling? (in hours) " ))
    distance =  velocity*hours
    return distance

distance = calculate_distance()
print ("The total distance you travelled is ", distance, "miles")
