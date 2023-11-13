from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), 
    path('add', views.add_todo, name = 'add'),
    path('update/<int:todo_id>/', views.update_todo, name = 'update'),
    path('delete/<int:todo_id>/', views.delete_todo, name = 'delete')
]