#Finding a Protein Motif
#Objective: To determine which proteins have N-glycosylation, and their locations in the sequence.

#Step1: Parse input file from Rosalind

import sys
filename=sys.argv[1]
with open(filename, 'r') as f:
    old_ids = [l.strip() for l in f.readlines()]
    ids= [i[:6] for i in old_ids ]
    # print(mylist)
    # print(ids)

#Step 2: Obtain protein sequences from Uniprot IDs

from urllib import request

proteins={}

for i in range(len(ids)):
    
    resp=request.urlopen(f'https://www.uniprot.org/uniprot/{ids[i]}.fasta')
    tmp_data=resp.read().decode('UTF-8')
    tmp_list=tmp_data.split('\n')

    for line in tmp_list:
        if '>' in line:
            proteins[old_ids[i]]=''
        else:
            proteins[old_ids[i]] += line
        

#now we have a dictionary, in which the keys are the old labels that came from Rosalind, and the values are the AA sequences
#next, we need to see if the magic sequence is found in the sequences and if so at which locations

import re
G_pattern = re.compile(r'(?=(N[^P][ST][^P]))')

id_loc={}
for i in old_ids:
    locs=[]
    for m in G_pattern.finditer(proteins[i]):
        locs.append(str(m.start()+1))
    id_loc[i]=locs

for i in id_loc:
    if len(id_loc[i])!=0:
        print(i, '\n' + ' '.join(id_loc[i]))
        