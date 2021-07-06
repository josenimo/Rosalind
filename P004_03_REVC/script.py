#!/usr/bin/python

import sys
filename=sys.argv[1]
#print('Reading '+filename)

file=open(filename,'r')
DNA=str(file.read())
#print('DNA:'+DNA[:10])

DNAc=DNA.translate(str.maketrans("ATCG","TAGC"))
#print ('DNAc:'+DNAc)

revDNAc=DNAc[len(DNAc)::-1]
#print('revDNAc:'+revDNAc)
print(revDNAc)