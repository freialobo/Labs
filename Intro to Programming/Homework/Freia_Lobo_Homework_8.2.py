#Freia Lobo - fll220@nyu.edu - Homework #8 Problem #2
try:
    infile = open('answers.txt','r')
    filecontents = infile.readline()
    test_answers = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C']
    student_answers = []
    while filecontents != '':
        student_answers.append(filecontents.rstrip('\n'))
        filecontents = infile.readline()
    infile.close()
    score = 0
    for i in range (len(test_answers)):
        if (test_answers[i] == student_answers[i]):
            score+=1
    percentage_score = (score/len(test_answers))*100
    print("Your percentage score is ",percentage_score,"%")
except IOError:
    percentage_score = 0
    print("Your percentage score is ",percentage_score,"%")
    
    
