import os
import csv
import codecs

current_path = os.path.dirname(__file__)
target_path = os.path.join(current_path, 'csv', 'list-sjis.csv')
fp = codecs.open(target_path, 'r', 'shift_jis')
reader = csv.reader(fp, delimiter=',', quotechar='"')
for cells in reader:
    print(cells[1], cells[2])
