
import sys,re,urllib,requests
from bs4 import BeautifulSoup as bs

############### Fonctions à utiliser ###############
def checkInterval(interval):
	global start,end
	if re.match('[A-Z]-[A-Z]',interval) and interval[0]<=interval[2]:
		start = interval[0]
		end = interval[2]
	else:
		print('invalid interval :(\n')
		exit()

def checkPort(port):
	if(int(port)<0 or int(port)>1023):
		print('invalid port :(\n')
		exit()
	else:
		print('valid port :D\n')

	return port

def bs4ToString(data):
	for i in range(len(data)):
		data[i] = str(data[i])
	return data

def ListToString(list):
	string=''
	for i in list:
		str = i + ',.N+subst\n'
		string = string + str
	return string
###################################################

if(len(sys.argv)>1): #le user a ajouté des arguments
	checkInterval(sys.argv[1].upper())
	port = checkPort(sys.argv[2])
else: #le user n'a pas ajouté des arguments (par défaut)
	start = 'A'
	end = 'Z'
	port= '80'

file = 'vidal-Sommaires-Substances-'
path = 'http://localhost:'+ port + '/' + file

info = open('info1.txt','w')

meds = []
nbrTotal = 0
while(start<=end):
	url = path + start + '.htm'

	result = requests.get(url)
	html = bs(result.text.encode('latin1').decode(),'html.parser') #encode() et decode() sont pour corriger les chars spéciaux
	
	data = html.find_all('li')
	data = bs4ToString(data) #convertir les élements BS en String

	nbr = 0
	for i in data: #filtrer data pour laisser que les substances
		if '<a href=\"Substance/' in i: #substance
			med = re.findall('.htm">(.+)</a>',i)
			meds.append(med[0])
			nbr += 1
		else:
			data.remove(i) #non substance

	nbrTotal += nbr
	info.write("Nombre d'entité de " + start + " = " + str(nbr) + '\n') #sauvgarder le nombre d'entités cet lettre

	print('\nURL = "' + url + '" : Process completed !\n')

	start = chr(ord(start)+1) #incremeter la lettre

info.write("----------------------------\n")
info.write("Nombre total d'entité = " + str(nbrTotal)) #sauvgarder le nombre total d'entités
info.close()

substances = ListToString(meds) #convertir la Liste en une seule String pour l'écrire dans 'subst.dic'

open('subst.dic','w',encoding='utf-16le').write('\ufeff' + substances)

print('subst.dic is created.')