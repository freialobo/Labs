#Freia Lobo - fll220@nyu.edu - Homework #8 Problem #3
n = int(input("How many high scores do you want? "))
scores = [["Winner95", 200],["Selena", 1000],["PlayaHata", 400], ["Jon", 500], ["Arifur", 300]]

def print_top_scores(scores,n):
    for i in range (len(scores)):
        scores[i].reverse()
    scores.sort()
    scores.reverse()

    for i in range(n):
        scores[i].reverse()
    for i in range(n):
        print(scores[i][0],scores[i][1])

print_top_scores(scores,n)
