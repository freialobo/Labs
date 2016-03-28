#Freia Lobo - fll220@nyu.edu - Homework #8, Problem #1
def get_numbers():
    while True:
        try:
            number_1 = int (input ("Enter the smaller number "))
            break
        except ValueError:
            print("That was not a valid number! Try again...")
        except TypeError:
            print("That was not an integer! Try again...")
        
        
    while True:
        try:
            number_2 = int (input ("Enter the larger number "))
            break
        except ValueError:
            print("That was not a valid number! Try again...")
        except TypeError:
            print("That was not an integer! Try again...")
    return number_1,number_2

def division(number_1,number_2):
    try:
        quotient = (number_2)//(number_1)
    except ZeroDivisionError:
            print("You cannot divide by zero!")
            get_numbers()
    try:
        remainder = number_2%number_1
    except ZeroDivisionError:
            print("You cannot divide by zero!")
            get_numbers()
    print("The quotient is",quotient,"The remainder is", remainder)
print ("Enter two whole numbers, such that the first number is smaller than the second to get the quotient and the remainder")
n1, n2=get_numbers()
division(n1,n2)

