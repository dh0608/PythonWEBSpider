from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./test.html'), 'lxml')
for item in soup.select('li'):
    print(item['class'][0])
