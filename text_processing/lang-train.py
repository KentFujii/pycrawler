from sklearn import svm, metrics
from os import path
import glob
import re
import json


def check_freq(fname):
    name = path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    cnt = [0 for n in range(0, 26)]
    code_a = ord('a')
    code_z = ord('z')
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n - code_a] += 1
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    return (freq, lang)


def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {'freqs': freqs, 'labels': labels}


current_path = path.dirname(__file__)
data = load_files(current_path + '/source/lang/train/*.txt')
test = load_files(current_path + '/source/lang/test/*.txt')
with open(current_path + '/source/freq.json', 'w', encoding='utf-8') as fp:
    json.dump([data, test], fp)

clf = svm.SVC()
clf.fit(data['freqs'], data['labels'])

predict = clf.predict(test['freqs'])

ac_score = metrics.accuracy_score(test['labels'], predict)
cl_report = metrics.classification_report(test['labels'], predict)
print('正解率 =', ac_score)
print('レポート =')
print(cl_report)
