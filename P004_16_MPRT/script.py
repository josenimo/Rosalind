#Finding a Protein Motif
#Objective: To determine which proteins have N-glycosylation, and their locations in the sequence.

#Step1: Parse input file from Rosalind

import sys
filename=sys.argv[1]
with open(filename, 'r') as f:
    oldlabel = [l.strip() for l in f.readlines()]
    ids= [i[:6] for i in oldlabel ]
    # print(mylist)
    # print(ids)

#Step 2: Obtain protein sequences from Uniprot IDs

import subprocess
#obtain protein fastas using bash's curl
with open('proteins.txt', 'w') as f:
    for i in ids:
        p1=subprocess.run(['curl','-s',f'https://www.uniprot.org/uniprot/{i}.fasta'], stdout=f , text=True)

#creating dictionary {protein id: amino acid sequence string}

with open('proteins.txt', 'r') as f:
    FASTAfile = [l.strip() for l in f.readlines()]

FASTADict = {}
FASTALabel =''

for line in FASTAfile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line

newdict={}

for i in range(len(oldlabel)):
    tmp=''
    for x in FASTADict:
        if ids[i] in x:
            tmp=(FASTADict[x])
            break
    newdict[oldlabel[i]]=tmp
  
print(newdict['B5ZC00'][117:121])
#now we have a dictionary, in which the keys are the old labels that came from Rosalind, and the values are the AA sequences
#next, we need to see if the magic sequence is found in the sequences and if so at which locations