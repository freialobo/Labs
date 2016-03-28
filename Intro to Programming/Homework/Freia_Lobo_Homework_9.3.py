#Freia Lobo - fll220@nyu.edu - Homework #9 Problem #3

#reading the file and making it a list
infile = open('receipt.txt','r')
words = infile.read()
words_list = words.split()
infile.close()

def count_word_freq(list1):
    
    dictionary = {}

    for word in list1:
        count = list1.count(word)
        dictionary[word] = count
    return dictionary

wordcount = count_word_freq(words_list)
print(wordcount)


