import seaborn as sns
import matplotlib.pyplot as plt
import pandas

penguins = sns.load_dataset('penguins')
penguins = penguins.dropna()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='species', style='species', palette='Set1')
plt.title("Розподіл ваги та висоти пінгвінів")
plt.xlabel("Маса тіла (у грамах)")
plt.ylabel("Довжина крил (в мілі)")
plt.legend(title="Вид")
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=penguins, x='species', y='flipper_length_mm', palette='Set2')
plt.title("Розміри крил у залежності від виду пінгвіна")
plt.xlabel("Вид")
plt.ylabel("Довжина крил (мм)")
plt.show()

correlation_matrix = penguins.drop(columns=['species', 'island', 'gender']).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Катра кореляції пінгвінів")
plt.show()