from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm


def todo_view(request):

    context = {"tasks": Task.objects.all(),
               'form': TaskForm()}
    return render(request, 'todo/index.html', context)


def add_task(request):
    new_task = Task(title=request.POST.get('title'))
    new_task.save()
    return HttpResponseRedirect("/")


def delete_task(request, task_id):
    task_to_delete = Task.objects.get(id=task_id)
    task_to_delete.delete()
    return HttpResponseRedirect("/")


def update_task(request, task_id):
    task = Task.objects.get(id=task_id),

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task[0])
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
    context = {
        "task": task[0],
        "form": TaskForm(instance=task[0]),
    }
    return render(request, 'todo/update_task.html', context)


def delete_all(request):
    task = Task.objects.all().delete()
    return HttpResponseRedirect("/")

def delete_completed(request):
    task = Task.objects.filter(completed=True).delete()
    return HttpResponseRedirect("/")
