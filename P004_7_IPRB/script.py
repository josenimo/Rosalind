from os import uname
import sys
def readFile(filePath):
    #Reading a file and returning a list of lines#
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

sample=readFile(sys.argv[1])
digits=sample[0].split()
#k homozygous dominant
#m heterozygous
#n homozygous recessive

k=int(digits[0])
m=int(digits[1])
n=int(digits[2])

def undirected_edges(nodes):
    return ((nodes*(nodes-1))/2)
#homozygous Dominant edges
#between each other
k1=undirected_edges(k)
#edges from k to m and n
k2=(m+n)*k
kTotal=k1+k2

#edges between m, 3/4 probs
m1=undirected_edges(m)
#edges between m and n, 1/2 probs
m2=(m*n)

#probs 0 
n1=undirected_edges(n)

total_nodes=k+m+n
total_edges=kTotal+m1+m2+n1
prob1=((kTotal/total_edges)*1)+((m1/total_edges)*0.75)+((m2/total_edges)*0.5)

print (prob1)