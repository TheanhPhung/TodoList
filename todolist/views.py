from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView 
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from .models import Task, Subtask
from .form import TaskForm

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
    form_class = TaskForm
    template_name = "todolist/create_task.html"
    success_url = reverse_lazy("index")
