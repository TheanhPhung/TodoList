from django.urls import path

from . import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("task/<int:pk>", views.TaskDetailView.as_view(), name="task"),
    path("subtask/<int:task_id>", views.SubtaskListView.as_view(), name="subtasks"),
    path("create_task/", views.TaskCreateView.as_view(), name="create_task"),
]
