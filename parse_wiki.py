from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Telnet"
r = requests.get(url)
wiki = BeautifulSoup(res.text,"lxml")
elems = wiki.select('p')
for i in range(len(elems)):
    print(elems[i].getText())
soup = BeautifulSoup(r.content)
#print(soup.prettify)
heading = soup.find(id='See_also')
print(heading)
teams = heading.find_next('ul')
for team in teams:
    print(team.string)
