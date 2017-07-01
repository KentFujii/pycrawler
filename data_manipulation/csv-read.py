import os
import codecs


current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'csv', 'list-sjis.csv')
csv = codecs.open(target_path, 'r', 'shift_jis').read()

data = []
rows = csv.split('\n')
for row in rows:
    if row == '':
        continue
    cells = row.split(',')
    data.append(cells)

for c in data:
    print(c[1], c[2])
