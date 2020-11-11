from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_view, name='list'),
    path('add', add_task),
    path('delete/<int:task_id>', delete_task),
    path('update/<int:task_id>', update_task, name="update")
]


