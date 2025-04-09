from django.urls import path
from .views import PredictLoanApproval, predict_form

urlpatterns = [
    path("predict/", PredictLoanApproval.as_view()),
    path("predict-form/", predict_form, name="predict-form"),
]
