import os
from bs4 import BeautifulSoup

current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'html', 'eki-link.html')
html = open(target_path, encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('a[href]')
result = []

for a in links:
    href = a.attrs['href']
    title = a.string
    result.append((title, href))

print(result)
