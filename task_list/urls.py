

from django.urls import path
from task_list import views


urlpatterns = [
     path('', views.index, name='home'),
     path('contact/', views.contact, name='contact'),
        path('about/', views.about, name='about'),
        path('tasks/', views.tasks, name='tasks'),
]
 