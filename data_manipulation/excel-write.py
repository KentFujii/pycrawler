import os
import openpyxl

current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'csv', 'population.xlsx')
book = openpyxl.load_workbook(target_path)
sheet = book.active
total = 0
for i, row in enumerate(sheet.rows):
    if i == 0:
        continue
    po = int(row[2].value)
    total += po
print('total=', total)
sheet['A49'] = 'Total'
sheet['C49'] = total
c = sheet['C49']
c.font = openpyxl.styles.Font(size=14, color='FF0000')
c.number_format = sheet['C48'].number_format
target_path = os.path.join(current_path, 'csv', 'population-total.xlsx')
book.save(target_path)
print('OK')
