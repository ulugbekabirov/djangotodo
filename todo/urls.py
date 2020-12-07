from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_view, name='list'),
    path('add', add_task, name='add'),
    path('delete/<task_id>', delete_task, name="delete"),
    path('update/<task_id>', update_task, name="update"),
    path('delete_all', delete_all, name="delete_all"),
    path('delete_completed', delete_completed, name="delete_completed"),

    path('api/', TaskList.as_view(), ),
    path('api/<int:pk>', TaskItem.as_view(), ),

]


