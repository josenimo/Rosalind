import sys
#acquiring file from bash
filename=sys.argv[1]

#file as file object
file=open(filename,'r')

#DNA as string
DNA=str(file.read())

#dict for translation using ASCII codes
#84=T 85=U
mydict ={84:85}

#translate
RNA= DNA.translate(mydict)

print (RNA)
