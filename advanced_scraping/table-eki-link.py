import os
from bs4 import BeautifulSoup

current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'html', 'eki-link.html')
html = open(target_path, encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')

result = []

table = soup.select_one('table')

tr_list = table.find_all('tr')
for tr in tr_list:
    result_row = []
    td_list = tr.find_all(['td', 'th'])
    for td in td_list:
        cell = td.get_text()
        result_row.append(cell)
    result.append(result_row)


with open('tag.csv', mode="w") as f:
    for row in result:
        column = ','.join(row)
        f.write(column + '\n')
        print(column)
print('保存しました')
