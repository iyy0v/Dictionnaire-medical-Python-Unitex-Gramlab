# Dictionnaire Médical (Python + Unitex/Gramlab)
I made this project for my **Information Extraction** class during the 1st semester of my 3rd Bachelor year (L3).

## Objective :
- Scrape all HTML files containing VIDAL.FR's mediactions and generate a dictionary ***subst.dic*** of those medications using ***extraire.py***.
    - Generate ***infos1.txt*** containing mediaction data of the medications in ***subst.dic***.
- Enrich the dictionary with new medical entities from ***corpus-medical.txt*** using ***enrichir.py***.
    - Medications found in ***corpus-medical.txt*** will be stored in a new dictionary called ***subst_corpus.dic***.
    - Generate ***infos2.txt*** containing medication data obtained from the corpus.
    - Generate ***infos3.txt*** containing medication data obtained from the enrichment.
- Create an extraction graphe ***posologie.grf*** in UNITEX in order to extract medications occurences from ***corpus-medical.txt***. The result of the extraction will be stored by UNITEX in '*corpus-medical_snt > concord.html*'.
- Exploit the previous graph by calling UNITEX using ***unitex.py***.
- Inject the content of ***concord.html*** into an SQLite database called ***extraction.db*** using ***sqlite.py***.

You can find more details in the assignment ['Projet Extraction d'Information.pdf'](https://github.com/iyy0v/Dictionnaire-medical-Python-Unitex-Gramlab/blob/main/Projet%20Extraction%20d'Information.pdf) above.

## Prerequisites :
Before you start running the scripts, make sure you start an Apache server first using [XAMPP](https://www.apachefriends.org) or [EasyPHP Devserver](https://www.easyphp.org/easyphp-devserver.php), reconfigure the http port if you want to (default is **80**), then copy the HTML files from the VIDAL folder to the server's folder. <br /><br />
Now you should be able to access those pages from your browser using: <br /><br />
`http://localhost:[port]/[filename]` or `http://127.0.0.1:[port]/[filename]`<br /><br />
**example:** <br />
`http://1ocalhost:80/vidal-Sommaires-Substances-A.htm` <br />

## Usage :
Scripts MUST be run in the following order :

1. Run ***extraire.py***, which takes two **optional** arguments being the letters interval you want to process and the http port that your Apache server is running on. <br /><br />
   `py extraire.py [letters interval] [http port]` <br /><br />
   **example:** <br />
   `py extraire.py B-W 80` <br /><br />
   **PS:** If no arguments are given, the default interval is **A-Z** and the default port is **80**.<br /><br />
   
2. Run ***enrichir.py***, which takes the path to *corpus-medical.txt* as an argument (optional). <br /><br />
`py enrichir.py [path]` <br /><br />
**PS:** If no argument is given, the default path will be ***'corpus-medical.txt'***.<br /><br />

3. Create ***posologie.grf*** from *corpus-medical.txt* using UNITEX then extract the result.<br /><br />

4. Run ***unitex.py***. <br /><br />
`py unitex.py` <br /><br />
   
5. Run ***sqlite.py***, which takes the path to *concord.html* as an argument (optional). <br /><br />
`py sqlite.py [path]` <br /><br />
**PS:** If no argument is given, the default path will be ***'corpus-medical_snt/concord.html'***. <br />

## Languages and Tools :
__Languages:__ Python <br /><br />
__Libraries:__ sys, os, re, urllib, requests, bs4, sqlite3, locale, functools <br /><br />
__Tools:__ Unitex/Gramlab

\-

You can also check out the rest of my school projects [here](https://github.com/iyy0v/USTHBProjects).

\-

Created by [@iyy0v](https://www.ayoub-dev.com) - feel free to contact me !
