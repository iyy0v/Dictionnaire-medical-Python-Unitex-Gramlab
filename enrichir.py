import sys,re,locale
from functools import cmp_to_key

locale.setlocale(locale.LC_ALL, "fr_FR")

def ListToString(list):
    string=''
    for i in list:
        string = string + i
    return string

if(len(sys.argv) == 2):
	path = sys.argv[1]
else: #emplacement par défaut
	path = 'corpus-medical.txt'


corpus = open(path,'r',encoding='utf-8').read()

subst_corpus = re.findall(r'([A-Z][A-Za-z]{4,})\s[:,]?\s?(\d*[,.]\d+|\d+|½)\s?(g|mg|µg|mcg|ml|µl|ui|iu|ml|mol|mmol|cp|amp|flacon|G|MG|ΜG|MCG|ML|ΜL|UI|IU|ML|MOL|MMOL|CP|AMP)[\s,./:]', corpus)

newSubst = []

for i in subst_corpus:
    newSubst.append(i[0].lower() + ',.N+subst\n')

subst = open('subst.dic','r',encoding='utf-16le').readlines()
subst[0] = subst[0][1:] #enlever le BOM pour le tri (puis l'ajouter a l'écriture)

newSubstSorted = list(set(newSubst))
newSubstSorted.sort()

#La difference entre corpus et subst.dic
diff = [item for item in newSubstSorted if item not in subst]

subst = subst + newSubst #ajouter les nouvelles substances
subst = list(set(subst))
#Trier selon la langue fancaise
subst = sorted(set(newSubstSorted).union(set(subst)), key=cmp_to_key(locale.strcoll))

subst = ListToString(subst)
open('subst.dic','w',encoding='utf-16le').write('\ufeff' + subst)

print('subst.dic was modified.')

newSubst = ListToString(newSubst)
open('subst_corpus.dic','w',encoding='utf-16le').write('\ufeff' + newSubst)

print('subst_corpus.dic is created.')

# Remplir info2.txt
info2 = open('info2.txt','w')
nbrTotal = 0
data = {}
for i in sorted(newSubstSorted, key=cmp_to_key(locale.strcoll)):
    c = i[0].upper()

    if(c == 'é'):
        c = 'e'

    if(data.__contains__(c)):
        data[c] += 1
    else:
        data[c] = 1
    nbrTotal += 1

for lettre in data.keys():
    info2.write("Nombre d'entité de " + lettre + " = " + str(data[lettre]) + "\n")

info2.write("----------------------------\n")
info2.write("Nombre total d'entité = " + str(nbrTotal)) #sauvgarder le nombre total d'entités
info2.close()

print('info2.txt is created.')

# Remplir info3.txt
info3 = open('info3.txt','w')
nbrTotal = 0
data = {}
for i in sorted(diff, key=cmp_to_key(locale.strcoll)):
    c = i[0].upper()

    if(c == 'é'):
        c = 'e'

    if(data.__contains__(c)):
        data[c] += 1
    else:
        data[c] = 1
    nbrTotal += 1

for lettre in data.keys():
    info3.write("Nombre d'entité de " + lettre + " = " + str(data[lettre]) + "\n")

info3.write("----------------------------\n")
info3.write("Nombre total d'entité = " + str(nbrTotal)) #sauvgarder le nombre total d'entités
info3.close()

print('info3.txt is created.')
