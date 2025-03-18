import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Завантаження даних
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, header=None, names=column_names)

print("Перегляд перших рядків:")
print(df.head())
print("\nСередня довжина чашелистика для кожного виду:")
print(df.groupby("class")["sepal_length"].mean())

print("\nМаксимальна ширина листка для виду 'setosa':")
print(df[df["class"] == "Iris-setosa"]["petal_width"].max())

print("\nРозподіл довжини листка для всіх ірисів:")
sns.histplot(df["petal_length"], bins=20, kde=True)
plt.show()
df_versicolor = df[df["class"] == "Iris-versicolor"]
print("\nДані для виду 'versicolor':")
print(df_versicolor.head())

df_filtered = df[df["petal_length"] > 5.0]
print("\nІриси з довжиною листка більше 5.0:")
print(df_filtered.head())

print("Середня ширина листка для кожного виду:")
print(df.groupby("class")["petal_width"].mean())

print("Мінімальна довжина чашелистика для кожного виду:")
print(df.groupby("class")["sepal_length"].min())

mean_petal_length = df["petal_length"].mean()
df_count = df[df["petal_length"] > mean_petal_length].groupby("class")["petal_length"].count()

print("Кількість ірисів кожного виду, що мають довжину листка більше за середню:")
print(df_count)