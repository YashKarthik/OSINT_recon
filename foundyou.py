import requests
import re
from bs4 import BeautifulSoup

class colors:
	MAGENTA = '\033[95m'
	GREEN = '\033[92m'
	STOP = '\033[0m'
	RED='\033[31m'
    
un = str(input(colors.MAGENTA+("Enter the username: ")))

def insta():
	uname = "https://instagram.com/"+str(un)
	reponse = requests.get(uname)
	soup = BeautifulSoup(reponse.text, 'html.parser')
	if soup.findAll(text = re.compile('Sorry, this page isn\'t available.')): 
	     print(colors.RED+(u'\u2716'+" Instagram account not found")+colors.STOP)
	else:
	     print(colors.GREEN+(u'\u2713' + " Instagram account found")+colors.STOP)

def fb():
	uname = ("https://facebook.com/"+str(un))
	response = requests.get(uname)
	soup = BeautifulSoup(response.text, 'html.parser')
	if response.status_code == 404 : 
	     print(colors.RED+(u'\u2716'+" Facebook account not found")+colors.STOP)
	else:
	     print(colors.GREEN+(u'\u2713' + " Facebook account found")+colors.STOP)

def git():
	uname = "https://github.com/"+str(un)
	response = requests.get(uname)
	soup = BeautifulSoup(response.text, 'html.parser')
	if response.status_code == 404 : 
	    print(colors.RED+(u'\u2716'+" GitHub account not found")+colors.STOP)
	else:
	    print(colors.GREEN+(u'\u2713' + " GitHub account found")+colors.STOP)

insta()
fb()
git()