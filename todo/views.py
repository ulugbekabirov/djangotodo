from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task
from .forms import TaskForm
from rest_framework import status

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


class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializers = TaskSerializer(tasks, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskItem(APIView):

    def get(self, request, pk):
        # task = Task.objects.get(id=pk)
        task = get_object_or_404(Task, pk=pk)
        serializers = TaskSerializer(task, many=False)
        return Response(serializers.data)

    def put(self, request, pk):
        # task = Task.objects.get(id=pk)
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        data = TaskSerializer(task).data
        task.delete()
        return Response(data)
