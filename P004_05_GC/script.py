#Step1: Read the data from file
import sys
def readFile(filePath):
    #Reading a file and returning a list of lines#
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
    #GC content in DNA/RNA seq#
    return round(((seq.count('C')+seq.count('G')) /len(seq) *100),6)

#Storing file into a list of strings
FASTAfile= readFile(sys.argv[1])
#Dictionary for labels + Data
FASTADict = {}
#String for holding the current label
FASTALabel =''

#print(FASTAfile)

#Step2: Clean data for operation
for line in FASTAfile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line

#print(FASTADict)

#Step3:Format data in usable form
RESULTDict = {key:gc_content(value) for (key, value) in  FASTADict.items()}
#print (RESULTDict)

#Step4:Run operations
MaxCGKey = max(RESULTDict, key=RESULTDict.get)

#Step5: Collect results

print(f'{MaxCGKey[1:]}\n{RESULTDict[MaxCGKey]}')