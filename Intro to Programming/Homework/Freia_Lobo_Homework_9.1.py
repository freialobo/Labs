#Freia Lobo - fll220@nyu.edu - Homework #9 Problem #1
word = input ("Enter an infinitive " )
if word[-1] == 'y':
    new_word = word[:-1] + "ies"
#o,ch,s,sh,xorz,addes
if word[-1] == 'o' or word[-2:] == 'ch' or word[-1] == 's' or word[-2:] == 'sh' or word[-1] == 'x' or word[-1] == 'z':
    new_word = word + "es"
else:
    new_word = word[:-1] + "s"
print (new_word)
