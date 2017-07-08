from os import path
from sklearn import svm, metrics
import random, re


def str_to_num(num):
    if re.match(r'^[0-9\.]+$', num):
        return float(num)
    else:
        return num


csv = []
target_path = path.dirname(__file__) + '/csv/iris.csv'
with open(target_path, 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        cols = list(map(str_to_num, cols))
        csv.append(cols)

del csv[0]
print(csv)
