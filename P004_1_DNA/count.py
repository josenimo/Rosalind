#Creating file object from text file
file = open("rosalind_dna.txt","r")

#Creating string variable from file object
string = file.read()

#Counting characters in string
mylist = []
for i in ['A','C','G','T']:
    mylist.append(str(string.count(i)))

print(" ".join(mylist))