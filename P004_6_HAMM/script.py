import sys

def readFile(filePath):
    #Reading a file and returning a list of lines#
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

DNA=readFile(sys.argv[1])

#print (DNA)

Counter=0

for i,j in zip(DNA[0],DNA[1]):
    if i!=j:
        Counter+=1

print (Counter)