from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import TodoItem
from django.contrib.auth.decorators import login_required
# import user
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        todos = TodoItem.objects.filter(creator=request.user)
    else:
        todos = TodoItem.objects.filter(creator__isnull=True)
    return render(request, 'todo/index.html', {'items': todos})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        todo = TodoItem.objects.create(title=title, creator=request.user if request.user.is_authenticated else None)
        return render(request, 'todo/todo_item.html', {'it': todo})
    return HttpResponse(status=405, content='Method Not Allowed')

def validate(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        if TodoItem.objects.filter(title=title).exists():
            return HttpResponse('<span class="text-red-500">Title already exists</span>')
        return HttpResponse('')

    return HttpResponse(status=405, content='Method Not Allowed')

def update(request, id):
    todo = get_object_or_404(TodoItem, pk=id)
    if request.method == 'PATCH':
        todo.completed = not todo.completed
        todo.save()
        return render(request, 'todo/todo_item.html', {'it': todo})
    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse('')
    return HttpResponse(status=405, content='Method Not Allowed')
