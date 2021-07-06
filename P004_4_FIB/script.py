import sys
filename=sys.argv[1]
file=open(filename,'r')
input=str(file.read())
mylist=input.split()
#print('printing list')
#print(mylist)

n=int(mylist[0])
k=int(mylist[1])

memory= [0,1,1]

for i in range(3,n+1):
    x = memory[-1] + (memory[-2]*k)
    memory.append(x)

print (memory[-1])
