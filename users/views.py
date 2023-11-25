from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('project_list')
    else:
        register_form = RegisterForm()
    
    return render(request, 'register.html', {'form': register_form})

