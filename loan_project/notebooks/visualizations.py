import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("loan_data.csv")
df.fillna(df.mode().iloc[0], inplace=True)
df["Loan_Status"] = df["Loan_Status"].map({"N": 0, "Y": 1})

plt.figure(figsize=(6, 4))
sns.countplot(x="Loan_Status", data=df)
plt.title("Розподіл статусу кредиту")
plt.xlabel("Loan Approved (1 = Yes, 0 = No)")
plt.ylabel("Кількість")
plt.tight_layout()
plt.show()

numeric_cols = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term"]
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f"Розподіл: {col}")
    plt.tight_layout()
    plt.show()

for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x="Loan_Status", y=col, data=df)
    plt.title(f"{col} залежно від Loan_Status")
    plt.tight_layout()
    plt.show()

plt.figure(figsize=(10, 8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Кореляційна матриця")
plt.tight_layout()
plt.show()
