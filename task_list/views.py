from django.http import HttpResponse
from django.shortcuts import render

from task_list.models import Task
from task_list.form import TaskForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'tasklist.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def tasks(request):
    all_tasks = Task.objects.all()
    context = {
        'tasks': all_tasks
    }
    return render(request, 'tasks.html', context)

def task_add(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully')
           
        else:
            messages.error(request, 'Error adding task')
            return render(request, 'form.html', {'form': form})
       
    form = TaskForm()
        
    return render(request, 'form.html', {'form': form})