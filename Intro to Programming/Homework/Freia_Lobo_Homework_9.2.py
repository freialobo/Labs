#Freia Lobo - fll220@nyu.edu - Homework #9 - Problem #2
new_word = ''
original = input('Enter a word: ')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == 'a' or first == 'e'or first == 'i' or first == 'o' or first == 'u':
        new_word = word+'ay'
        print (new_word)
    else:
        new_word = word[1:]+first+'ay'
        print ("The pig latin version is " +new_word)
else:
    original = input("Enter a word :")
