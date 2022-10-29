import requests
from pyfiglet import Figlet
import re
import sys

class couleur:
		  	OK = '\033[91m' 
		  	ba= '\033[92m' 
		  		

figlet = Figlet(font='slant')
result = figlet.renderText("Ys jhonson")
dak= figlet.renderText("Le wana")

print(couleur.OK+result)
print(couleur.OK+dak)
print(couleur.ba+'WebParamScanner [++++++]')

try :
	
	
	param = sys.argv[2]
	file = open(param, 'r')
	for list in file:
		a = list.strip()
		so = sys.argv[1]
		req  = requests.get(so)
		dab = req.content
	
		if a in str(dab):
			class couleur:
			 	OK = '\033[91m'
			 	ba= '\033[92m' 
			print(couleur.ba+str(req.url)+'?'+a)
		
				
except :
	print('python paramweb.py site.com/page.php param.txt')

			
				
					
