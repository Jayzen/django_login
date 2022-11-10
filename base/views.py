from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth import login


def home(request):
    return render(request, 'base/home.html', {})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

