import requests
from bs4import BeautifulSoup

site =requests.get('https://fr.wikipedia.org/wiki/Prince_(musicien)')
soup = BeautifulSoup(site.text, 'html.parser')

for section in soup.find_all('li', attrs={'class':'toclevel-1tocsection-1'});
	print(section.text)