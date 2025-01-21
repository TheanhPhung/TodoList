from django.urls import path

from . import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("task/<int:pk>", views.TaskDetailView.as_view(), name="task"),
    path("subtask/<int:task_id>", views.SubtaskListView.as_view(), name="subtasks"),
    path("create_task/", views.TaskCreateView.as_view(), name="create_task"),
    path("create_subtask/<int:task_id>", views.SubtaskCreateView.as_view(), name="create_subtask"),
    path("update_task/<int:pk>", views.UpdateTaskView.as_view(), name="update_task"),
    path("complete_task/<int:task_id>", views.CompleteTaskView.as_view(), name="complete_task"),
]
