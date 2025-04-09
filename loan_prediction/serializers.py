from rest_framework import serializers

class LoanApplicationSerializer(serializers.Serializer):
    Gender = serializers.CharField()
    Married = serializers.CharField()
    Dependents = serializers.CharField()
    Education = serializers.CharField()
    Self_Employed = serializers.CharField()
    ApplicantIncome = serializers.FloatField()
    CoapplicantIncome = serializers.FloatField()
    LoanAmount = serializers.FloatField()
    Loan_Amount_Term = serializers.FloatField()
    Credit_History = serializers.FloatField()
    Property_Area = serializers.CharField()
