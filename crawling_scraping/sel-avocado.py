import os
from bs4 import BeautifulSoup

current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'html', 'fruits-vegetables.html')
fp = open(target_path, encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

print(soup.select_one('li:nth-of-type(8)').string)
print(soup.select_one('#ve-list > li:nth-of-type(4)').string)
print(soup.select('#ve-list > li[data-lo="us"]')[1].string)
print(soup.select('#ve-list > li.black')[1].string)

cond = {'data-lo': 'us', 'class': 'black'}
print(soup.find('li', cond).string)
print(soup.find(id='ve-list').find('li', cond).string)
