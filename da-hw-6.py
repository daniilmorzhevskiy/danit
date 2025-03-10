import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


penguins = sns.load_dataset('penguins')


penguins = penguins.dropna()


penguins_encoded = pd.get_dummies(penguins, drop_first=True)
X = penguins_encoded.drop('species_Adelie', axis=1)

y = penguins_encoded['species_Adelie']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()), 
    ('classifier', RandomForestClassifier(random_state=42)) 
])

scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"Cross-validation accuracy: {scores.mean()}")

pipeline.fit(X_train, y_train)

accuracy = pipeline.score(X_test, y_test)
print(f"Test accuracy: {accuracy}")

param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [10, 20, 30],
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

print(f"Best hyperparameters: {grid_search.best_params_}")

y_pred = grid_search.predict(X_test)

print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Adelie', 'Chinstrap', 'Gentoo'], yticklabels=['Adelie', 'Chinstrap', 'Gentoo'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()