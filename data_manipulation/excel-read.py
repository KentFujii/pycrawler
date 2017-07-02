import os
import openpyxl

current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'csv', 'population.xlsx')
book = openpyxl.load_workbook(target_path)

sheet = book.worksheets[0]
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[2].value
    ])
del data[0]
data = sorted(data, key=lambda x: x[1])
for i, a in enumerate(data):
    if (i >= 5):
        break
    print(i + 1, a[0], int(a[1]))
