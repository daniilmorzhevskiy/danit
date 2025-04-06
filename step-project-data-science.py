import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Завантаження даних
print("Loading data...")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. Попередній огляд
print(df.head())

# 3. Заповнення пропущених значень
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# 4. Інженерія ознак
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr', 'Major',
                                   'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')

# 5. Кодування категоріальних змінних
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
df = pd.get_dummies(df, columns=['Embarked', 'Title'], drop_first=True)

# 6. Видалення непотрібних стовпців
df = df.drop(['Ticket', 'Cabin', 'Name', 'PassengerId'], axis=1)

# 7. Візуалізація (EDA)
sns.countplot(x='Survived', data=df)
plt.title('Розподіл виживших')
plt.show()

sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Виживання за класом')
plt.show()

sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Виживання за статтю')
plt.show()

sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True)
plt.title('Виживання за віком')
plt.show()

sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Виживання за вартістю квитка')
plt.show()

# 8. Кореляційна матриця
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Матриця кореляцій")
plt.show()

# 9. Підготовка даних
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 10. Модель 1 — Логістична регресія
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
y_pred1 = logreg.predict(X_test)

print("\n=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, y_pred1))
print("Classification Report:\n", classification_report(y_test, y_pred1))

# 11. Модель 2 — Випадковий ліс
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred2 = rf.predict(X_test)

print("\n=== Random Forest ===")
print("Accuracy:", accuracy_score(y_test, y_pred2))
print("Classification Report:\n", classification_report(y_test, y_pred2))

# 12. Матриця помилок
conf = confusion_matrix(y_test, y_pred2)
sns.heatmap(conf, annot=True, fmt='d')
plt.title("Confusion Matrix - Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# 13. Крос-валідація
cv_scores_logreg = cross_val_score(logreg, X, y, cv=5)
cv_scores_rf = cross_val_score(rf, X, y, cv=5)

print("\nCross-validation (Logistic Regression):", cv_scores_logreg.mean())
print("Cross-validation (Random Forest):", cv_scores_rf.mean())

# 14. Підбір гіперпараметрів для Random Forest
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [4, 6, 8],
}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid.fit(X_train, y_train)

print("\nBest Parameters (Random Forest):", grid.best_params_)
best_rf = grid.best_estimator_
print("Test Accuracy (Best RF):", accuracy_score(y_test, best_rf.predict(X_test)))
