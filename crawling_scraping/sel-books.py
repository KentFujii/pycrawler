import os
from bs4 import BeautifulSoup
target_path = os.path.join(os.path.dirname(__file__), 'html', 'books.html')
fp = open(target_path, encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')


def sel(query):
    print(soup.select_one(query).string)


sel('#nu')
sel('li#nu')
sel('ul > li#nu')
sel('#bible #nu')
sel('#bible > #nu')
sel('ul#bible > li#nu')
sel('li[id="nu"]')
sel("li:nth-of-type(4)")

print(soup.select('li')[3].string)
print(soup.find_all('li')[3].string)
