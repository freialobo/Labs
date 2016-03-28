#Freia Lobo - Oct 22 - In Class Assignment - #2
def are_earlier_in_alphabet(w,list_of_words):
    new_list = []
    for x in list_of_words:
        if x<w:
            new_list = new_list + [x]
    return new_list
a = input ("Enter the word you want to compare with the list ").lower()
b= ["cashew","apple","winebago","app","taco","spider","chalk","window","tornado","masquerade"]
smaller_words = are_earlier_in_alphabet(a,b)
print ('The words in the list that come before',a,"are",smaller_words)
