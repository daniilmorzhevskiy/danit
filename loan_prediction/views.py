from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import joblib
from django.shortcuts import render
import requests

model = joblib.load('loan_model.pkl')

class PredictLoanApproval(APIView):
    def get(self, request):
        data = {
            'Gender': request.GET.get('Gender'),
            'Married': request.GET.get('Married'),
            'Dependents': request.GET.get('Dependents'),
            'Education': request.GET.get('Education'),
            'Self_Employed': request.GET.get('Self_Employed'),
            'ApplicantIncome': float(request.GET.get('ApplicantIncome', 0)),
            'CoapplicantIncome': float(request.GET.get('CoapplicantIncome', 0)),
            'LoanAmount': float(request.GET.get('LoanAmount', 0)),
            'Loan_Amount_Term': float(request.GET.get('Loan_Amount_Term', 0)),
            'Credit_History': float(request.GET.get('Credit_History', 0)),
            'Property_Area': request.GET.get('Property_Area')
        }
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return Response({'prediction': prediction})
    


def predict_form(request):
    prediction = None
    if request.GET:
        url = 'http://127.0.0.1:8000/api/predict/'
        response = requests.get(url, params=request.GET)
        if response.status_code == 200:
            data = response.json()
            prediction = 'Одобрено' if data['prediction'] == 1 else 'Отказано'
    return render(request, 'loan_prediction/form.html', {'prediction': prediction})

