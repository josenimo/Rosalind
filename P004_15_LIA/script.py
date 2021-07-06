import sys
filename=sys.argv[1]
with open(filename, 'r') as f:
    mylist=list(f)
    # print('mylist: ' + str(mylist))
    x=str(mylist[0])
    # print('x: '+ str(x))
    y=x.strip().split(' ')
    # print(y)
    generation=int(y[0])
    number=int(y[1])
    final_pop=2**generation

    # print(final_pop)
    # print(k, n)

import math
# print(math.factorial(3))
def fac(x):
    return math.factorial(x)

prob=0
for i in range(number,final_pop+1):
    prob+=fac(final_pop)/((fac(i)*fac((final_pop-i)))) * (0.25**i) * (0.75**(final_pop-i))

print(round(prob,3))

#Research
#All three mixes: AA, Aa, aa x Aa: have 50% chance of producing a 'Aa' genotype
#Thus, all possible two-allelic genotype mixed with a double heterozygous has a 25% chance to produce a heterozygous offspring.
#AaBb x anything has 0.25 of being AaBb
#generations how many children, how many children times 0.25 is how many offspring in that generation would likely be AaBb
#but we must answer the probability to see "amount_wanted"