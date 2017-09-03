import pandas as pd
from sklearn import svm, model_selection
from os import path

target_path = path.dirname(__file__) + '/../iris.csv'
csv = pd.read_csv(target_path)

data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
label = csv['Name']

clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print('各正解率', scores)
print('正解率 =', scores.mean())
