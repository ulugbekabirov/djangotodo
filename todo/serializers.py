from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
    created = serializers.DateField(required=False)
    completed = serializers.BooleanField(required=False, default=False)