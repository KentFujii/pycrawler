from sklearn import svm, metrics
from sklearn.externals import joblib
from os import path
import json

targetpath = path.dirname(__file__)
with open(targetpath + '/source/freq.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
    data = d[0]

with open(targetpath + '/source/freq.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
    test = d[1]


clf = svm.SVC()
clf.fit(data['freqs'], data['labels'])

predict = clf.predict(test['freqs'])
ac_score = metrics.accuracy_score(test['labels'], predict)
print(ac_score)


joblib.dump(clf, targetpath + '/cgi-bin/freq.pkl')
print('ok')

clf_re = joblib.load(targetpath + '/cgi-bin/freq.pkl')
predict_re = clf_re.predict(test['freqs'])
ac_score_re = metrics.accuracy_score(test['labels'], predict_re)

print(ac_score_re)
