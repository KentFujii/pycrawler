import os
import pandas as pd

current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'csv', 'population.xlsx')
sheet_name = 'list-sjis.csv'
book = pd.read_excel(target_path, sheetname=sheet_name)
book.sort_values(by='法定人口', ascending=False)
print(book)
