from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email = email, password = password, username = username)
            login(request, user)
            return redirect('home')

    context = {
        'form_user' : form
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        user=form.get_user()
        if user:
            login(request,user)
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request,'users/user_login.html',context)

def reset(request):
    return render(request, 'users/reset.html')
