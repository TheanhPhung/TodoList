from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView 


from .models import *


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todolist/index.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "todolist/task.html"
