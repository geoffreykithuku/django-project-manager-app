import datetime

from django.shortcuts import redirect, render

from task_list.models import Task, Project
from task_list.app_forms import TaskForm, ProjectForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user).order_by('-created_at')
    
    pagination = Paginator(projects, 3)
    page = request.GET.get('page')
    projectsObj = pagination.get_page(page)
    
    
    all_projects = []
    
    for project in projectsObj:
        data = {}

        data['item'] = project
        data['all'] = project.tasks.all().count()
        data['complete'] = project.tasks.filter(completed=True).count()
        data['incomplete'] = project.tasks.filter(completed=False).count()
        if data['all'] > 0:
           data['percent'] = round((data['complete'] / data['all']) * 100)
        else:
           data['percent'] = 0
           
        data['days_left'] = (project.due_date - datetime.date.today()).days

        all_projects.append(data) 
        
    
    
    return render(request, 'project_list.html', {'projects': all_projects, 'pages': projectsObj})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'project_form.html', {'form': form})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all()
    pagination = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    
    return render(request, 'project_detail.html', {'project': project, 'tasks': page_obj})

@login_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect('project_list')

@login_required
def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project.save()
            return redirect('project_detail', project_id=project_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProjectForm(instance=project)
        
    return render(request, 'project_form.html', {'project': project, 'form': form} )
@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all()
    return render(request, 'task_list.html', {'project': project, 'tasks': tasks})

@login_required
def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.owner = request.user
            task.save()
            return redirect('project_detail', project_id=project_id)
        else:
            messages.error(request, 'Please correct the error below.')
            print(form.errors)
    else:
        
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form, 'project': project})


@login_required
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

@login_required                                          
def task_delete(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('project_detail', project_id=project_id)