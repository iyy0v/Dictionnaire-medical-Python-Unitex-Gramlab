# Dictionnaire Medical (Python + Unitex/Gramlab)
I made this project for my **Information Extraction** class during my 3rd Bachelor year (L3).

## Objective
- Scrape all HTML files containing VIDAL.FR's mediactions and generate a dictionary **subst.dic** of those medications using **extraire.py**.
    - Generate **infos1.txt** containing mediaction data of the medications in **subst.dic**.
- Enrich the dictionary with new medical entities from **corpus-medical.txt** using **enrichir.py**.
    - Medications found in **corpus-medical.txt** will be stored in a new dictionary called **subst_corpus.dic**.
    - Generate **infos2.txt** containing medication data obtained from the corpus.
    - Generate **infos3.txt** containing medication data obtained from the enrichment.
- Create an extraction graphe **posologie.grf** in UNITEX in order to extract medications occurences from **corpus-medical.txt**. The result of the extraction will be stored by UNITEX in **corpus-medical_snt > concord.html**.
- Exploit the previous graph by calling UNITEX using **unitex.py**.
- Inject the content of **concord.html** into an SQLite database called **extraction.db** using **sqlite.py**.

You can find more details in the assignment ["Projet Extraction d'Information.pdf"](https://github.com/iyy0v/Dictionnaire-medical-Python-Unitex-Gramlab/blob/main/Projet%20Extraction%20d'Information.pdf) above.

## Languages and Tools:
__Languages:__ Python <br>
__Libraries:__ sys, os, re, urllib, requests, bs4, sqlite3, locale, functools <br>
__Tools:__ Unitex/Gramlab <br>
  
<br/>
You can also check out the rest of my school projects [here](https://github.com/iyy0v/USTHBProjects/).
