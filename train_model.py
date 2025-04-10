import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
import joblib

df = pd.read_csv("loan_data.csv")
df.fillna(df.mode().iloc[0], inplace=True)

X = df.drop(columns=["Loan_ID", "Loan_Status"])
y = df["Loan_Status"].map({"N": 0, "Y": 1})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numeric_features = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
categorical_features = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

# pipeline test, need to recheck
classifier = RandomForestClassifier(random_state=42)
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", classifier)
])

pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "loan_model.pkl")

def plot_feature_importance(model, feature_names, output_path):
    importances = model.feature_importances_
    feature_series = pd.Series(importances, index=feature_names).sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_series, y=feature_series.index, palette="viridis")
    plt.title("Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Features")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

ohe = pipeline.named_steps["preprocessor"].named_transformers_["cat"]
encoded_cat_features = ohe.get_feature_names_out(categorical_features)
all_features = numeric_features + list(encoded_cat_features)

os.makedirs("visualizations", exist_ok=True)
plot_feature_importance(classifier, all_features, "visualizations/feature_importance.png")
