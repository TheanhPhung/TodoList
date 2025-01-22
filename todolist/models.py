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
    deadline = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="not_start")
    priority = models.IntegerField(default=0, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.name
    
    def estimated_progress(self):
        subtasks_list = Subtask.objects.filter(node=self)
        total_score = 0
        progress_score = 0
        for subtask in subtasks_list:
            total_score += subtask.progress_score
            if subtask.complete == True:
                progress_score += subtask.progress_score
        
        if progress_score > 0:
            if progress_score < total_score:
                self.status = "in_progress"
                self.save()
            else:
                self.status = "completed"
                self.save()

        return 0 if total_score == 0 else progress_score / total_score * 100
        

class Subtask(models.Model):
    name = models.CharField(max_length=100)
    node = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="child_subtasks")
    progress_score = models.IntegerField(default=1)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
