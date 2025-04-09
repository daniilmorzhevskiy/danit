import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV

# Загрузка данных
df = pd.read_csv("loan_data.csv")

# Заполнение пропущенных значений
df.fillna(df.mode().iloc[0], inplace=True)

# Разделение признаков и целевой переменной
X = df.drop(columns=["Loan_ID", "Loan_Status"])  # Используем все признаки
y = df["Loan_Status"].map({"N": 0, "Y": 1})  # Преобразуем целевую переменную

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Определение категориальных и числовых признаков
numeric_features = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
categorical_features = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]

# Предобработка данных
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Создание конвейера с моделью
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Параметры для GridSearchCV
param_grid = {
    "classifier__n_estimators": [50, 100, 200],
    "classifier__max_depth": [None, 10, 20],
    "classifier__min_samples_split": [2, 5, 10]
}

# Подбор гиперпараметров
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid_search.fit(X_train, y_train)

# Результаты
print("Лучшие параметры:", grid_search.best_params_)
print("Точность на обучающем наборе:", grid_search.best_estimator_.score(X_train, y_train))
print("Точность на тестовом наборе:", grid_search.best_estimator_.score(X_test, y_test))