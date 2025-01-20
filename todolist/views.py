from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView 
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from .models import Task, Subtask
from .form import TaskForm, SubtaskForm

from .models import *


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todolist/index.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "todolist/task.html"


class SubtaskListView(ListView):
    template_name = "todolist/subtasks.html"

    def get_queryset(self):
        task = get_object_or_404(Task, id=self.kwargs["task_id"])
        return task.child_subtasks.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=self.kwargs["task_id"])
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/create_task.html"
    success_url = reverse_lazy("index")


class SubtaskCreateView(CreateView):
    model = Subtask
    form_class = SubtaskForm
    template_name = "todolist/create_subtask.html"

    def get_success_url(self):
        return reverse_lazy("subtasks", kwargs={"task_id": self.kwargs["task_id"]})
