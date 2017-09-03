from os import path
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

target_path = path.dirname(__file__) + '/../iris.csv'
csv = pd.read_csv(target_path)

csv_data = csv[
    ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']
]
csv_label = csv['Name']

train_data, test_data, train_label, test_label = train_test_split(csv_data,
                                                                  csv_label)

clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("正解率 =", ac_score)
