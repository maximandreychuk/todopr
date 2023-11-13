from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import ToDo


def index(request):

    todo_lst = ToDo.objects.all()
    return render(request, 'todoapp/index.html', 
                  {'todo_lst_key': todo_lst,
                   'title': 'Главная страница'})

@require_http_methods(['POST'])
def add_todo(request):

    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')

def update_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    # todo.save()
    return redirect('index')