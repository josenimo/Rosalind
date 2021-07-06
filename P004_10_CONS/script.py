#obtain the consensus sequence from 1<n<10 Fasta sequences
from os import TMP_MAX
import sys
import pandas as pd
import numpy as np
#obtain file
def readFile(filePath):
    #Reading a file and returning a list of lines#
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

#organize Fasta sequences in Dict
#Storing file into a list of strings
FASTAfile= readFile(sys.argv[1])
#Dictionary for labels + Data
FASTADict = {}
#String for holding the current label
FASTALabel =''
#for loop that creates a dict with labels as keys and the seq. data as values.
for line in FASTAfile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line

sequences=list(FASTADict.values())
length=len(sequences[0])
# print(FASTADict)
# print(FASTADict['>Rosalind_7'])
#create matrix, each nucleotide a list

sequences_A=[]
sequences_T=[]
sequences_C=[]
sequences_G=[]

nucleotides=['A','T','C','G']

def sequence_binary(nucleotide,listtoappendto):
    "sequences_{nucleotide}"
    #using nucleotide as a string
    for i in sequences:
        #for every sequence in the list of sequences
        #string1 is the temporary string denoting the boolean status of each nucleotide
        string1=''
        #print('i: '+ str(i))

        for j in range(length):
            #j being each nucleotide in the sequence i
            #print('j: ' + str(j))
            if i[j]== nucleotide:
                string1 += '1'
            else:
                string1 += '0'
        #appending the string1(current boolean string) to list of strings, each string a sequence.
        listtoappendto.append(string1)    


sequence_binary('A',sequences_A)
sequence_binary('T',sequences_T)
sequence_binary('C',sequences_C)
sequence_binary('G',sequences_G)

matrix_list_A=[]
matrix_list_T=[]
matrix_list_C=[]
matrix_list_G=[]

def binary_sequence_sum (binary_list, matrixlist):
    
    for position in range(length):
        tmp_position_value=0
        #print('position: ' + str(position))
        for sequence in binary_list:
            #print('sequence: ' + str(sequence))
            if sequence[position]=='1':
                tmp_position_value+=1
        matrixlist.append(tmp_position_value)

binary_sequence_sum(sequences_A,matrix_list_A)
binary_sequence_sum(sequences_T,matrix_list_T)
binary_sequence_sum(sequences_C,matrix_list_C)
binary_sequence_sum(sequences_G,matrix_list_G)

consensus=[]
dict_matrix={}

dict_matrix['A']=matrix_list_A
dict_matrix['C']=matrix_list_C
dict_matrix['G']=matrix_list_G
dict_matrix['T']=matrix_list_T


for position in range(length):
    # print('pos: ' + str(position))
    tmpmax=0
    for dict_key in dict_matrix:
        # print('  dict_key: ' + str(dict_key))
        
        if tmpmax < int(dict_matrix[dict_key][position]):
            tmpmax = int(dict_matrix[dict_key][position])
        # print('    tmpmax' + str(tmpmax))
    for dict_key in dict_matrix:
        # print('      2ndloop'+str(dict_key))
        if int(dict_matrix[dict_key][position])==tmpmax:
            consensus.append(dict_key)
            # print('consensus: ' + ' '.join(map(str,consensus)))
            break

# print('   '+' '.join(map(str,consensus)))
print(''.join(map(str,consensus)))

print('A: ' + ' '.join(map(str,matrix_list_A)))
print('C: ' + ' '.join(map(str,matrix_list_C)))
print('G: ' + ' '.join(map(str,matrix_list_G)))
print('T: ' + ' '.join(map(str,matrix_list_T)))

# nucleotides=['A','T','C','G']


#solution from Rosalind
# def cons(strings):
#     from collections import Counter
#     counters = map(Counter, zip(*strings))
#     consensus = "".join(c.most_common(1)[0][0] for c in counters)
#     profile_matrix = "\n".join(b + ": " + \
#         " ".join(str(c[b]) for c in counters) for b in "ACGT")
#     return consensus + "\n" + profile_matrix

#solution2 from Rosalind
# strands = [x.strip() for x in f.readlines()]

# matrix = zip(*strands)

# profile_matrix = map(lambda x: dict((base, x.count(base)) for base in "ACGT"), matrix)

# consensus = [max(x,key = x.get) for x in profile_matrix]

# print "".join(consensus);

# for base in "ACGT":
#     print base+":",
#     for x in profile_matrix:
#         print x[base],
#     print ""