from bs4 import BeautifulSoup

soup = BeautifulSoup(open('alice.html'), 'html.parser')

print soup.title
print soup.title.string
print soup.p
print soup.p['class']
print soup.find_all('a')
print soup.find(id='link3')