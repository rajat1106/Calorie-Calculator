from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def measure(request):
    return render(request,'Measure.html')

def account(request):
    return render(request,'Account.html')

def bmi(request):
    return render(request,'BMI.html')

def bmr(request):
    return render(request,'BMR.html')