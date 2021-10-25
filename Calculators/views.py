from django.shortcuts import redirect, render
from Calculators.models import Users
from django.contrib.auth.models import User,auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name = name, password=password, email=email, username=username)
                user.save()
                return redirect('login')

        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')


    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def bmi(request):
    welcome = Users.objects.all()
    return render(request, 'bmi.html', {'message': welcome})


def bmr(request):
    return render(request, 'bmr.html')


def fat(request):
    return render(request, 'fat.html')


def calories(request):
    return render(request, 'calories.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
