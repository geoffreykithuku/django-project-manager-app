from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    register_form = UserCreationForm()
    
    return render(request, 'register.html')


def signin(request):
    return render(request, 'signin.html')