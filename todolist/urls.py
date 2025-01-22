from django.urls import path

from . import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("completed_task", views.CompletedTaskListView.as_view(), name="completed_tasks"),
    path("task/<int:pk>", views.TaskDetailView.as_view(), name="task"),
    path("subtask/<int:task_id>", views.SubtaskListView.as_view(), name="subtasks"),
    path("create_task/", views.TaskCreateView.as_view(), name="create_task"),
    path("create_subtask/<int:task_id>", views.SubtaskCreateView.as_view(), name="create_subtask"),
    path("update_task/<int:pk>", views.UpdateTaskView.as_view(), name="update_task"),
    path("update_subtask/<int:pk>", views.UpdateSubtaskView.as_view(), name="update_subtask"),
    path("complete_task/<int:pk>", views.CompleteTaskView.as_view(), name="complete_task"),
    path("delete_task/<int:pk>", views.DeleteTaskView.as_view(), name="delete_task"),
    path("complete_subtask/<int:pk>", views.CompleteSubtaskView.as_view(), name="complete_subtask"),
    path("delete_subtask/<int:pk>", views.DeleteSubtaskView.as_view(), name="delete_subtask"),
]
