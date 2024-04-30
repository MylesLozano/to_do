from django.shortcuts import render, redirect
from todo.models import AddItem

def todo_list(request):
    todos = AddItem.objects.all()  # Get all todos
    context = {'todos': todos}
    return render(request, 'todo/todo_list.html', context)  # Render index.html with todos

def add_todo(request):
    if request.method == "POST":
        title_name = request.POST.get('title_name')
        todo_description = request.POST.get('todo_description')
        todo_deadline = request.POST.get('todo_deadline')
        todo = AddItem(title_name=title_name, todo_description=todo_description, todo_deadline=todo_deadline)
        todo.save()
        return redirect('todo_list')  # Redirect back to the todo list (index)
    return render(request, 'todo/add_todo.html')  # Render add_todo form

def update_todo(request, id):
    todo = AddItem.objects.get(id=id)
    if request.method == "POST":
        todo.title_name = request.POST.get('title_name')
        todo.todo_description = request.POST.get('todo_description')
        todo.todo_deadline = request.POST.get('todo_deadline')
        todo.save()
        return redirect('todo_list')  # Redirect back to the todo list (index)
    return render(request, 'todo/update_todo.html', {'todo': todo})  # Render update form

def delete_todo(request, id):
    todo = AddItem.objects.get(id=id)
    todo.delete()
    return redirect('todo_list')  # Redirect back to the todo list (index)