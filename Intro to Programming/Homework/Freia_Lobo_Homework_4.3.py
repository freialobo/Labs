#Freia Lobo - fll220@nyu.edu - Homework #4, Problem #3
def get_hourly_wage():
    local_hourly_wage = float (input("What is your hourly wage? "))
    return local_hourly_wage

def get_hours_worked():
     local_hours_worked = float(input("How many hours did you work? "))
     return local_hours_worked

def calculate_gross_pay(hourly_wage, hours_worked):
    if hours_worked <=40:
        local_gross_pay = hourly_wage*hours_worked
    else:
        local_gross_pay = (hourly_wage * 40) + ((1.5*hourly_wage)*(hours_worked-40))
    return local_gross_pay
def display_pay(grs_pay):
            grs_pay = format (grs_pay, ',.2f')
            print("Your total gross pay is ", grs_pay, sep = '$')
hourly_wage = get_hourly_wage()
hours_worked = get_hours_worked()
gross_pay = calculate_gross_pay (hourly_wage, hours_worked)
display_pay(gross_pay)

                           
