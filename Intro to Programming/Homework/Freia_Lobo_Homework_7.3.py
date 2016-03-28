infile = open('names.txt','r')
count = 0
name = "a"
while name != '':
    name = infile.readline()
    print (name)
    count+=1
infile.close()
print("The count is", count)
    
