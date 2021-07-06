import re
import sys
import numpy
# #plan
# 1. obtain both strings

def readFile(filePath):
    #Reading a file and returning a list of lines#
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
lines=readFile(sys.argv[1])
s=str(lines[0])
t=str(lines[1])

# 2. somehow rolling windows across string
locs=[i for i in range(len(s)) if s.startswith(t,i)]

# since they are using 1-based counting we must add1 to each locations
array= numpy.array(locs)
array=array+1

locs=array.tolist()
locs_str=map(str,locs)
print(' '.join(locs_str))