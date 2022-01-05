'''
#count how many phrases are there

import sys
text=open("80jours.snt",'r', encoding='utf-8')
n=1
for i in text:
    n+= i.count('{S}')
    
print(n)
'''

'''
#convert utf-8 to utf-16 LE with BOM

import codecs
var = codecs.open("old.txt",'r','utf-8').read()
codecs.open("new.txt",'w','utf-16le').write('\ufeff'+var) #.write('\ufeff') to add BOM
'''

'''
#convert utf-8 to utf-16 BE with BOM

import codecs
var = codecs.open("old.txt",'r','utf-8').read()
codecs.open("new.txt",'w','utf-16be').write('\ufeff'+var) #.write('\ufeff') to add BOM 
'''


'''
import sys,re,codecs
file = open("80jours.txt",'r',encoding='utf-16-le')
lines = file.readlines()
names = []
for line in lines:
    temp = re.findall("[A-Z][a-z]+ [A-Z][a-z]+",line)
    for name in temp:
        if name not in names:
            names.append(name)
print(names)
file.close()
'''

import os
from os import path
if path.exists("80jours_snt"):
    os.system("rd /s 80jours_snt")
os.mkdir("80jours_snt")
os.system("UnitexToolLogger Normalize 80jours.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize 80jours.snt")
os.system("UnitexToolLogger Dico -t 80jours.snt Dela_fr.bin")
os.system("UnitexToolLogger Grf2Fst2 context.grf")
os.system("UnitexToolLogger Locate -t 80jours.snt context.fst2 -L -I --all")
os.system("UnitexToolLogger Concord 80jours_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")
