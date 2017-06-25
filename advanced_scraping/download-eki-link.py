from urllib import parse, request
from bs4 import BeautifulSoup
import os
import time

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

savepath = './out'
if not os.path.exists(savepath):
    os.mkdir(savepath)

for title, url in result:
    path = savepath + '/' + url + '.html'
    print(url)
    a_url = parse.urljoin(
        'https://search.yahoo.co.jp', 'search?p=' + url)
    print('download=' + a_url)
    request.urlretrieve(a_url, path)
    time.sleep(1)
