from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView 
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, UpdateView

from .models import Task, Subtask
from .form import TaskForm, SubtaskForm

from .models import *


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todolist/index.html"

    def get_queryset(self):
        return Task.objects.exclude(status="completed")


class TaskDetailView(DetailView):
    model = Task
    template_name = "todolist/task.html"


class SubtaskListView(ListView):
    template_name = "todolist/subtasks.html"

    def get_queryset(self):
        task = get_object_or_404(Task, id=self.kwargs["task_id"])
        return task.child_subtasks.filter(complete=False)

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

    def form_valid(self, form):
        subtask = form.save(commit=False)
        subtask.node = get_object_or_404(Task, id=int(self.kwargs["task_id"]))
        subtask.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_id"] = self.kwargs["task_id"] 
        return context

    def get_success_url(self):
        return reverse_lazy("subtasks", kwargs={"task_id": self.kwargs["task_id"]})


class UpdateTaskView(UpdateView):
    model = Task
    fields = ["name", "description", "deadline", "status", "priority"]
    template_name = "todolist/task_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy("task", kwargs={"pk": self.kwargs["pk"]})


class CompleteTaskView(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        task = get_object_or_404(Task, id=int(pk))
        task.status = "completed"
        task.save()
        return redirect(reverse_lazy("index"))


class DeleteTaskView(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        task = get_object_or_404(Task, id=int(pk))
        task.delete()
        return redirect(reverse_lazy("index"))


class CompleteSubtaskView(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        subtask = get_object_or_404(Subtask, id=int(pk))
        subtask.complete = True
        subtask.save()
        node = subtask.node
        return redirect(reverse_lazy("subtasks", kwargs={"task_id": node.id}))


class DeleteSubtaskView(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        subtask = get_object_or_404(Subtask, id=int(pk))
        node = subtask.node
        subtask.delete()
        node = subtask.node
        return redirect(reverse_lazy("subtasks", kwargs={"task_id": node.id}))
