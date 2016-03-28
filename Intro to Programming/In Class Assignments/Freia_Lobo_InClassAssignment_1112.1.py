name = input("What is your username? ")
try:
    infile = open('username.txt','r')
    filecontents = infile.readline()
    list1= []
    while filecontents != '':
        list1.append(filecontents.rstrip('\n'))
        filecontents = infile.readline()
    infile.close()
    count = 0
    for i in range (len(list1)):
        if name == list1[i]:
            count+=1
    if count == 0:
        list1.append(name)
        list1.sort()
    else:
        list1.sort()
    outfile = open('username.txt','w')
    for i in range(len(list1)):
        outfile.write(list1[i] + '\n')
    outfile.close()
    print("Open username.txt for your sorted list")
except IOError:
    print("Sorry the file username.txt does not exist")
