#A bug tracking program

total_bugs = 0
day = 1
while day <=7:
    sentence = "How many bugs did you college on day "+ str(day) + "
    num_bugs = int(input("How manay bugs have you collected today? "))
    total_bugs += num_bugs
    day+=1
print ("The total number of bugs is", total_bugs)
