from django.urls import path
from .views import PredictLoanApproval, predict_form, home


urlpatterns = [
    path("", home, name="home"),
    path("predict/", PredictLoanApproval.as_view()),
    path("predict-form/", predict_form, name="predict-form"),
]
