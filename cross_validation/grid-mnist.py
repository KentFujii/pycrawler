import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import GridSearchCV
from os import path

target_train_path = path.dirname(__file__) + '/../mnist/train.csv'
target_t10k_path = path.dirname(__file__) + '/../mnist/t10k.csv'

train_csv = pd.read_csv(target_train_path)
test_csv = pd.read_csv(target_t10k_path)

train_label = train_csv.ix[:, 0]
train_data = train_csv.ix[:, 1:577]
test_label = test_csv.ix[:, 0]
test_data = test_csv.ix[:, 1:577]
print('学習データ数', len(train_label))

params = [
    {"C": [1, 10, 100, 1000], "kernel": ["linear"]},
    {"C": [1, 10, 100, 1000], "kernel": ["rbf"], "gamma": [0.001, 0.0001]}
]

clf = GridSearchCV(svm.SVC(), params, n_jobs=-1)
clf.fit(train_data, train_label)
print('学習器 =', clf.best_estimator_)

pre = clf.predict(test_data)
ac_score = metrics. accuracy_score(pre, test_label)
print('正解率 =', ac_score)
