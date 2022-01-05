import sys,re,sqlite3
from bs4 import BeautifulSoup as bs

def bs4ToString(data):
	for i in range(len(data)):
		data[i] = str(data[i])
	return data

if(len(sys.argv) == 2):
	path = sys.argv[1]
else: #emplacement par défaut
	path = 'corpus-medical_snt/concord.html'


html = open(path,'r',encoding='utf-8')

html = bs(html,'html.parser') 

data = html.find_all('a') #extraire les élements <a> qui contient les posologies
data = bs4ToString(data) #convertir les élements BS en String

posologies = []
for i in data: #mettre les posologies dans une liste
	pos = re.findall('">(.+)</a>',i)
	posologies.append(pos[0])


connect = sqlite3.connect('extraction.db') #creation et connection au database

cursor = connect.cursor() #selectionner la DB

cursor.execute('CREATE TABLE posologies (ID int, Posologie text)') #creation de la table

for i in range(len(posologies)): #insertions des élements dans la table
	cursor.execute('INSERT INTO posologies VALUES (?,?)',(i+1,posologies[i]))

connect.commit() #enregistrement des changements

connect.close() #fermeture du DB

print("extraction.db is created !")
