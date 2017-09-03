from os import path
from sklearn import svm, metrics


def load_csv(fname):
    labels = []
    images = []
    with open(fname, 'r') as f:
        for line in f:
            cols = line.split(',')
            if len(cols) < 2:
                continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {'labels': labels, 'images': images}


target_path = path.dirname(__file__) + '/../mnist/'
data = load_csv(target_path + 'train.csv')
test = load_csv(target_path + 't10k.csv')

clf = svm.SVC()
clf.fit(data['images'], data['labels'])

predict = clf.predict(test['images'])

ac_score = metrics.accuracy_score(test['labels'], predict)
cl_report = metrics.classification_report(test['labels'], predict)
print('正解率 =', ac_score)
print('レポート = ')
print(cl_report)
