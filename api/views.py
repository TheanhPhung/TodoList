from rest_framework import permissions, viewsets

from todolist.models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("deadline")
    serializer_class = TaskSerializer
    permissions_classes = [permissions.IsAuthenticated]


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
    permissions_classes = [permissions.IsAuthenticated]
