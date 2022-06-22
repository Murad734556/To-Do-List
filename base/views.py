from django.shortcuts import render, redirect
from .models import Task


def TaskList(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks,
    }
    return render(request, 'task_list.html', context)

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task.objects.create(title = title)
        task.save()
        return redirect('tasks')
    return render(request, 'task_create.html')

def task_update(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task.objects.get(id = id)
        task.title = title 
        task.save()
        return redirect('tasks')
    context = {
        'tasks': task,
    }
    return render(request, 'task_update.html')

def task_delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id = id)
        task.delete()
        return redirect('tasks')
    return render(request, 'task_delete.html')
    



  