#     AA-AA
#     AA-Aa
#     AA-aa
#     Aa-Aa
#     Aa-aa
#     aa-aa

import sys

filename=sys.argv[1]
with open(filename,'r') as f:
    x=list(f)
    couples=list(map(int,x[0].split(sep=' ')))

prob_list=[1,1,1,0.75,0.50,0]

E=0

for i in range(6):
    y = couples[i]*2
    E += y*prob_list[i]

print(E)

# Sum=0
# for i in couples:
#     Sum+=i

# print('Sum:' + str(Sum))