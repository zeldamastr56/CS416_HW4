from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)


@require_POST
def add(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        new_task = Task(task_item=request.POST['task_item'])
        new_task.save()

    return redirect('index')


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'tasks/delete.html', {'task': task})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'tasks/update.html', {'form': form})


def complete(request, id):
    task = Task.objects.get(id=id)
    task.complete = True
    task.save()

    return redirect('index')