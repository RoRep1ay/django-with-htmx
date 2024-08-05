from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import TodoItem


def home(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'items': todos})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print('title =', title)
        todo = TodoItem.objects.create(title=title)
        return HttpResponse(_render_item(todo))
    return HttpResponse(status=405, content='Method Not Allowed')

def validate(request):
    print('hello world', request.method)
    if request.method == 'GET':
        title = request.GET.get('title')
        print('title =', title)
        if TodoItem.objects.filter(title=title).exists():
            return HttpResponse('<span class="text-red-500">Title already exists</span>')
        return HttpResponse('')

    return HttpResponse(status=405, content='Method Not Allowed')

def update(request, id):
    todo = get_object_or_404(TodoItem, pk=id)
    if request.method == 'PATCH':
        todo.completed = not todo.completed
        todo.save()
        return HttpResponse(_render_item(todo))
    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse('')
    return HttpResponse(status=405, content='Method Not Allowed')


def _render_item(todo: TodoItem):
    checked_attr = ' checked' if todo.completed else ''
    return f"""<li class="flex items-center border-b border-gray-200 py-2" id="item-{todo.id}">
        <input
          type="checkbox" 
          class="mr-2"
          id="myCheckbox-{ todo.id }"
          hx-target="#item-{ todo.id }"
          hx-swap="outerHTML"
          hx-patch="/todos/{ todo.id }/"
          {checked_attr}
        > 
          <div class="flex justify-between items-center w-full">
            <span>{ todo }</span>
            <button
              hx-delete="/todos/{ todo.id }/"
              class="bg-red-500 text-white px-2 py-1 rounded"
              hx-swap="outerHTML"
              hx-target="#item-{ todo.id }"
            >
              Delete
          </button>
        </div>
      </li>"""
