import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv(r'traincsv.csv')

print(dataset.head(20))

X = dataset.iloc[:, 1:784].values
y = dataset.iloc[:, 0].values

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0)
# _____________________________----------------------------_____________________________----------------


model = RandomForestClassifier(n_estimators=1000)
model.fit(x_train, y_train)
ypre = model.predict(x_test)

print(metrics.classification_report(ypre, y_test))

mat = confusion_matrix(y_test, ypre)
print(mat)

