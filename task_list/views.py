from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tasklist.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
def tasks(request):
    return render(request, 'tasks.html')