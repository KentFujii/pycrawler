from os import path
import random
import re
from sklearn import svm, metrics


def str_to_num(num):
    return float(num) if re.match(r'^[0-9\.]+$', num) else num


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

random.shuffle(csv)

total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("正解率 =", ac_score)
