

from django.urls import path
from task_list import views


urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('<int:project_id>/delete/', views.project_delete, name='project_delete'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('<int:project_id>/tasks/create/', views.task_create, name='task_create'),
    path('<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:project_id>/tasks/<int:task_id>/update/', views.task_update, name='task_update'),
    path('<int:project_id>/tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]