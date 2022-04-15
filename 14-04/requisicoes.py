import requests, json
from bs4 import BeautifulSoup

r = requests.get('https://api.github.com/users/julianofischer')
j = json.loads(r.text)
#print(j)

#print(j['login'])
#print(j['id'])
#print(j['company'])

ifro = requests.get('https://portal.ifro.edu.br', verify=False)
#print(ifro.text)
soup = BeautifulSoup(ifro.text, 'html.parser')
#print(soup.prettify())
#print(soup.title.string)
tags = soup.find_all("div", {'class': 'listagem-chamadas-secundarias'})[0]
divs = tags.find_all('div', {'class': 'row-fluid'})
print(len(divs))
div1 = divs[0]
print(div1.p.text)

