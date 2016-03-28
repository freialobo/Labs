#Write a function that takes a percentage grade (0-100) as an argument and returns the letter grade.
#For example if your gunction was called get_letter_grade, a statement like get_letter_grade(75)
#would return c. Write a program that uses your function.


def percentage_to_letter( ):
    percentage_grade= int (input ("Enter your percentage grade "))
    if percentage_grade>=90:
        print ("Your grade is an A ")
    else:
            if percentage_grade >= 80:
                print ("Your grade is a B")
            else:
                        if percentage_grade >=70:
                                print ("Your grade is a C")
                        else:
                            if percentage_grade >= 60:
                                print ("Your grade is a D")
                            else:
                                    if percentage_grade >=50:
                                        print ("Your grade is an E")
                                    else:
                                                print ("Your grade is an F")

percentage_grade = percentage_to_letter( )


    
