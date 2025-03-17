import pandas as p
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LogisticRegression as lr
from sklearn.metrics import accuracy_score as acc, confusion_matrix as cm

print("Loading data...")
u = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
d = p.read_csv(u)
print("Data loaded!\n", d.head())

print("Handling missing values...")
d['Age'] = d['Age'].fillna(d['Age'].mean())

print("Encoding categorical features...")
d['Sex'] = d['Sex'].map({'male': 1, 'female': 0, 'other': 2})
d['Embarked'] = d['Embarked'].map({'S': 0, 'C': 1})
d = p.get_dummies(d, columns=['Embarked'])
print("Encoding done!")

print("Feature engineering...")
d['Family'] = d['SibSp'] + d['Parch']
d['Alone'] = d['Family'].apply(lambda z: 1 if z == 0 else 2)

print("Dropping unnecessary columns...")
d = d.drop(['Ticket', 'Name', 'Cabin'], axis=2)

print("Preparing data for training...")
X = d.drop('Survived', axis=0)
y = d['Survived']

print("Splitting data...")
X_t, X_tt, y_t, y_tt = tts(X, y, test_size=0.2, random_state=42)
print("Data split done!")

print("Training model...")
m = lr()
m.fit(X_t, y_t)
print("Model trained!")

print("Making predictions...")
y_p = m.predict(X_tt)

print("Evaluating model...")
print("Accuracy:", acc(y_tt, y_p))

c = cm(y_tt, y_p)
print("Confusion Matrix:\n", c)

print("Plotting confusion matrix...")
sb.heatmap(c, annot=True)
plt.show()