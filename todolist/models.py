from django.db import models

from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        ("not_start", "Not Start"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("canceled", "Canceled")
    ]

    PRIORITY_CHOICES = [
        (4, "Urgent and important"),
        (3, "Non urgent but important"),
        (2, "Urgent but not important"),
        (1, "Non urgent and non important")
    ]

    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    priority = models.IntegerField(default=0, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.name
    
    def estimated_progress(self):
        pass

class Subtask(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    progress_score = models.IntegerField(default=10)

    def __str__(self):
        return self.name
