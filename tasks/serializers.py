from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tasks.models import Task


class TaskSerializer(ModelSerializer):
    delayed = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = "__all__"
