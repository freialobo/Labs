#Freia Lobo - In Class Assignment - Oct 22 - #1
print ("This program will ask for 2 numbers, r and n and give you 1 + r + r^2 + r^3 + ... + r^n")
r = float(input("Enter the number 'r' " ))
n = int(input("Enter the number 'n' " ))
total = 0
for n in range (0,n+1):
    total +=(r**n)
print (total)

0.5
