from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['target'] = iris.target
data['species'] = data['target'].apply(lambda x: iris.target_names[x])
print(data.shape)
print(data.dtypes)
print(data.head(3))
print(iris.keys())
print(len(data))
print(data.columns)
print(iris.DESCR)
print(data.describe())
print(data['species'].value_counts())
sns.pairplot(data, hue='species')
plt.show()
data['species'].value_counts().plot(kind='bar')
plt.show()
X = data.iloc[:, :-2]
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train.shape, X_test.shape)
le = LabelEncoder()
data['target'] = le.fit_transform(data['species'])
X = data.iloc[:, :-2]
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, X_test.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
preds = knn.predict(X_test)
print(preds)
