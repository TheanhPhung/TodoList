from django import forms
from .models import Task, Subtask


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "deadline", "priority"]

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ["name", "deadline", "progress_score", "node"]
