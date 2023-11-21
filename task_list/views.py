from django.http import HttpResponse
from django.shortcuts import redirect, render

from task_list.models import Task
from task_list.form import TaskForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'tasklist.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def tasks(request):
    all_tasks = Task.objects.all()
    paginator = Paginator(all_tasks, 5)
    page = request.GET.get('page')
    data  = paginator.get_page(page)
    context = {
        'tasks': data
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

def delete(request, id):
    task = get_object_or_404(Task, pk=id)
    
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('tasks')

def edit(request, id):
    task = get_object_or_404(Task, pk=id)
    task.completed = not task.completed
    task.save()
    messages.success(request, 'Task edited successfully')
    return redirect('tasks')
    