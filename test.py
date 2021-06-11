f = open('writtentext.txt','r')
filelines = f.readlines()
for line in filelines :
    print(line)
f.read()



f.close()