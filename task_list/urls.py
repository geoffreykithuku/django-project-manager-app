

from django.urls import path
from task_list import views


urlpatterns = [
     path('', views.index, name='home'),
     path('contact/', views.contact, name='contact'),
        path('about/', views.about, name='about'),
        path('tasks/', views.tasks, name='tasks'),
        path('task_add/', views.task_add, name='task_add'),
        path('delete/<int:id>', views.delete, name='delete'),
        path('edit/<int:id>', views.edit, name='edit'),
]
 