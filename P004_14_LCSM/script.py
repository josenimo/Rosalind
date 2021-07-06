# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

import sys

def readFile(filePath):
    #Reading a file and returning a list of lines#
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

FASTADict={}
FASTALabel =''
FASTAfile= readFile(sys.argv[1])

for line in FASTAfile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line
        
listofFASTA=[]
for dict_key in FASTADict:
    listofFASTA.append(str(FASTADict[dict_key]))

#print(listofFASTA)  

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        #check that data has items in it
        for i in range(len(data[0])):
            #iteration over all starting positions
            for j in range(len(data[0])-i+1):
                #iteration over all possible lengths of substring taking into account starting positions
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    #if length of current substring is bigger than current 
                    #and if the substring starting at i with ending position at i+j is found in all items of data.
                    substr = data[0][i:i+j]
    return substr


def is_substr(find, data):
  """
  inputs a substring to find, returns True only 
  if found for each data in data list
  """

  if len(find) < 1 or len(data) < 1:
    return False # expected input DNE

  is_found = True # and-ing to False anywhere in data will return False
  for i in data:
    # print ("Looking for substring %s in %s..." % (find, i)) debugging only
    is_found = is_found and find in i
  return is_found

LCS = long_substr(listofFASTA)

print(LCS)
