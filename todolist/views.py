from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView


from .models import *


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todolist/index.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "todolist/task.html"


class SubtaskListView(ListView):
    context_object_name = "subtasks"
    template_name = "todolist/subtasks.html"

    def get_queryset(self):
        self.task = get_object_or_404(Task, id=self.kwargs["task_id"])
        return Subtask.objects.filter(node=self.task)


class TaskCreateView(CreateView):
    model = Task
    fields = ["name", "deadline", "description"]
    template_name = "todolist/create_task.html"
