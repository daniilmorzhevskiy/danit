
# Прогнозування Кредитоспроможності

## Опис проекту

Метою цього проекту є створення системи прогнозування схвалення кредиту на основі введених користувачем даних. Проект включає аналіз даних, розробку моделі машинного навчання, візуалізацію, створення веб-застосунку на Django та інтеграцію форми для взаємодії з користувачем.

---

## Структура проекту

```
loan_project/
├── loan_prediction/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── model.pkl
│   ├── templates/
│   │   └── form.html
│   ├── urls.py
│   └── views.py
├── loan_project/
│   └── settings.py, urls.py, etc.
├── manage.py, etc.
├── loan_data.csv
├── loan_model.pkl
└── visualizations/
    ├── feature_importance.png
    ├── loan_status_by_education.png
    ├── applicant_income_vs_loan_status.png
    ├── correlation_heatmap.png
    └── <other visualizations>.png
```

---

## Дані

- `loan_data.csv` — набір даних для тренування моделі
- Колонки:
  - Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Loan_Status

---

## Обробка даних

1. Завантаження та очищення даних
2. Заповнення відсутніх значень
3. Аналіз кореляцій між змінними

---

## Модель машинного навчання

- Алгоритм: RandomForestClassifier
- Інструменти: Pipeline, ColumnTransformer, GridSearchCV
- Збереження моделі у файл `loan_model.pkl`

---

## Веб-застосунок (Django)

### Запуск

```bash
python manage.py runserver
```

### Веб-інтерфейс

- **URL форми:** http://127.0.0.1:8000/api/form/
- **Що заповнювати:**
  - Gender: Male / Female
  - Married: Yes / No
  - Dependents: 0 / 1 / 2 / 3+
  - Education: Graduate / Not Graduate
  - Self_Employed: Yes / No
  - ApplicantIncome: числове значення
  - CoapplicantIncome: числове значення
  - LoanAmount: числове значення (у тисячах)
  - Loan_Amount_Term: 360 / 180 / 120 / інші
  - Credit_History: 1 (є) / 0 (немає)
  - Property_Area: Urban / Rural / Semiurban

- **Результат:** Після натискання "Submit" ви побачите прогноз: `1` — Схвалено, `0` — Відхилено

### API (curl)

```bash
curl "http://127.0.0.1:8000/api/predict/?Gender=Male&Married=Yes&Dependents=0&Education=Graduate&Self_Employed=No&ApplicantIncome=5000&CoapplicantIncome=0&LoanAmount=100&Loan_Amount_Term=360&Credit_History=1&Property_Area=Urban"
```

---

## Візуалізації

- Гістограми розподілу доходів заявника
- Кореляційна матриця теплової карти
- Розподіл статусу кредиту за категоріями
- Важливість ознак у моделі RandomForest

### Візуалізації будуть збережені в папці `visualizations`:
- `feature_importance.png`
- `loan_status_by_education.png`
- `applicant_income_vs_loan_status.png`
- `correlation_heatmap.png`
- та інші

---

## Використані бібліотеки

- pandas, numpy, seaborn, matplotlib
- sklearn (Pipeline, RandomForest, GridSearchCV)
- joblib (збереження моделі)
- Django

---

## Результати

- Точність моделі: ~80%
- Успішна інтеграція з веб-інтерфейсом
- Прогноз у реальному часі через curl або веб-форму

---

## Інструкція для користувача

1. Встановити залежності (віртуальне оточення):
```bash
pip install -r requirements.txt
```
2. Запустити сервер:
```bash
python manage.py runserver
```
3. Перейти до веб-форми: http://127.0.0.1:8000/api/form/
4. Заповнити дані та натиснути "Submit"
5. Або зробити запит через curl

---

## Автор

by D. Morzhevskyi

Проект створено в рамках навчального курсу з Python DanIT