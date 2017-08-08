from sklearn import model_selection, svm, metrics
import pandas as pd

tbl = pd.read_csv('bmi.csv')

label = tbl['label']
w = tbl['weight'] / 100
h = tbl['height'] / 200
wh = pd.concat([w, h], axis=1)

data_train, data_test, label_train, label_test = \
    model_selection.train_test_split(wh, label)

clf = svm.SVC()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print('正解率 =', ac_score)
print('レポート =\n', cl_report)