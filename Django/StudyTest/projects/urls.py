from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project1'),
    path('create-project', views.creteProject, name= 'create-project'),
    path('update-project/<str:pk>/', views.UpdateProject, name= 'update-project'),

    path('delete-project/<str:pk>/', views.deleteProject, name= 'delete-project'),

]
