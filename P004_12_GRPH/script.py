import sys
#process fasta into dict
def readFile(filePath):
    #Reading a file and returning a list of lines#
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
#Storing file into a list of strings
FASTAfile= readFile(sys.argv[1])
#Dictionary for labels + Data
FASTADict = {}
#String for holding the current label
FASTALabel =''

for line in FASTAfile:
    if '>' in line:
        FASTALabel = line[1:]
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line
        
k=3

# does right(3) of dict.value[1] == left(3) of for i in dict values not including self

mylist=[]
for i in FASTADict:
    mylist.append(str(i))
ML=[]

for i in mylist:
    
    others= [x for x in mylist if x != i]
    
    for o in others:
        tmplist=[]
        
        if FASTADict[i][-k:]==FASTADict[o][:k]:
            tmplist=[i,o]
            ML.append(tmplist)

            
for i in ML:
    print(' '.join(i))