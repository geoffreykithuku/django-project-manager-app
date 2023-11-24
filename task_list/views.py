from django.http import HttpResponse
from django.shortcuts import redirect, render

from task_list.models import Task, Project
from task_list.app_forms import TaskForm, ProjectForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, 'home.html')

def project_list(request):
    projects = Project.objects.all()
    
    return render(request, 'project_list.html', {'projects': projects})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'project_form.html', {'form': form})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all()
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})

def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect('project_list')


def task_list(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all()
    return render(request, 'task_list.html', {'project': project, 'tasks': tasks})

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project_id)
        else:
            messages.error(request, 'Please correct the error below.')
            print(form.errors)
    else:
        
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form, 'project': project})

def task_update(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            
            task.save()
            return redirect('project_detail', project_id=project_id)
        else:
            messages.error(request, 'Please correct the error below.')
            print(form.errors)
    
        
    return render(request, 'task_edit.html', {'task': task, 'project_id': project_id} )
                                                  
def task_delete(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('project_detail', project_id=project_id)